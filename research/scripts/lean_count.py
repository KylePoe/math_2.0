"""Monthly count of arXiv math submissions whose abstract mentions Lean/Mathlib.
Queries the arXiv API (cat:math.*, by submittedDate), downloads matching
abstracts, and keeps only those whose text matches a strict regex.
Usage: lean_count.py <out dir> [category query, default cat:math.*]"""
import re, sys, time, json, urllib.request, urllib.parse
import xml.etree.ElementTree as ET
OUT = sys.argv[1]
CAT = sys.argv[2] if len(sys.argv) > 2 else 'cat:math.*'
NS = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
LEAN = re.compile(r'\bMathlib\b|\bmathlib\b|\bLean\s?4\b|\bLean\s?3\b|Lean (theorem prover|proof assistant)'
                  r'|\b(in|into|using|with|within|via|the) Lean\b|formali[sz]\w*\s+(\w+\s+){0,3}in Lean')

def api(q, start=0, n=1):
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(
        {'search_query': q, 'start': start, 'max_results': n})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                root = ET.fromstring(r.read())
            time.sleep(3.2)
            return root
        except Exception as e:
            time.sleep(10)
    raise RuntimeError(q)

rows = []
months = [(y, m) for y in (2025, 2026) for m in range(1, 13) if not (y == 2026 and m > 10)]
for y, m in months:
    last = [31, 29 if y % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
    rng = f'submittedDate:[{y}{m:02d}010000 TO {y}{m:02d}{last}2359]'
    tot = int(api(f'{CAT} AND {rng}').find('o:totalResults', NS).text)
    q = f'{CAT} AND (abs:Mathlib OR abs:"Lean 4" OR abs:Lean) AND {rng}'
    root = api(q, 0, 1000)
    hits = int(root.find('o:totalResults', NS).text)
    entries = root.findall('a:entry', NS)
    ver = []
    for e in entries:
        txt = (e.find('a:title', NS).text or '') + ' ' + (e.find('a:summary', NS).text or '')
        txt = re.sub(r'\s+', ' ', txt)
        if LEAN.search(txt):
            ver.append({'id': e.find('a:id', NS).text, 'title': re.sub(r'\s+', ' ', e.find('a:title', NS).text)})
    rows.append(dict(month=f'{y}-{m:02d}', total=tot, api_hits=hits, fetched=len(entries), verified=len(ver), papers=ver))
    print(f'{y}-{m:02d} total {tot:6d}  api {hits:4d}  fetched {len(entries):4d}  verified {len(ver):4d}  ({100*len(ver)/tot:.2f}%)', flush=True)
json.dump(rows, open(f"{OUT}/lean_counts_{CAT.replace(':','_').replace('*','x')}.json", 'w'), indent=1)

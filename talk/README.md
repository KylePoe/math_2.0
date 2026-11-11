# Math 2.0: From Society to the Lab (slides)

A Beamer deck built on the Vidal Lab template. [`math-2.0-slides.pdf`](math-2.0-slides.pdf) is the finished PDF, one page per slide; [`RESOURCES.md`](RESOURCES.md) lists every link recommended in the talk.

## Build

```bash
latexmk main.tex
```

`.latexmkrc` selects XeLaTeX and writes to `build/`, so the PDF is `build/main.pdf`. The two AI-era timelines and the thesis slide are animated, so that PDF has one page per click. For the one-page-per-slide version:

```bash
latexmk -jobname=math-2.0-slides -usepretex='\PassOptionsToClass{handout}{beamer}' main.tex
```

## Structure

| Part | Sections | Files |
|---|---|---|
| Opening | Navier–Stokes; an emerging paradigm; Math 2.0 | `sections/00-*`, `01-*`, `02-*` |
| I. Society | Public reactions to Math 2.0; Open Societal Problems; Formalization; The Limits of Formalization | `sections/10-*` to `14-*` |
| II. The Lab | Tools and workflow; The Lean Blueprint; Statement Fidelity; Proof Fidelity | `sections/20-*` to `22-*` |
| Closing | Summary; open problems; three principles; resources | `sections/30-closing.tex` |
| Backup | Slides cut from the main flow, kept for questions | `sections/99-backup.tex` |

`main.tex` holds the preamble, the order of the sections and a time budget (45 minutes of content and 15 of discussion). Each section file has one frame per slide. The comment above each frame gives its timing, its sources and anything that still needed checking. To reorder the talk, reorder the `\input` lines in `main.tex`.

## Conventions

- The overview slide ("The rest of this talk") is generated from the `\part` and `\section` tree, so it follows any change to the structure. Part names are set once with `\partnameone` and `\partnametwo`.
- `\slidesources{...}` puts source credits in small grey type, running up the strip to the right of the body.
- The `keybox` TikZ style draws the emphasized box that ends many slides.
- `\sectionslide{Part I}{Society}` draws a divider slide.
- `\stub{minutes}{purpose}` prints a grey planning note; `\stubsfalse` in `main.tex` hides them all.
- `\resourcesurl` in `main.tex` is the address the QR code on the last slide encodes.

## Changes from the Vidal Lab template

- The title slide, divider slide and content slide are rebuilt with TikZ to follow the Penn Engineering PowerPoint layouts (`slide_formats/`). Only the two template images in use are kept.
- The content slide has a fixed title band and colour line, and a compact footer: author, short title and a breadcrumb (part › section) on the left, slide number and Penn logo on the right.
- If Open Sans isn't installed as a system font, the theme falls back to the copy in TeX Live.
- Frame titles are 15 pt; the body shares its left edge with the title and footer.

## Images

Third-party images (announcements, news headlines, Terence Tao's diagram and portrait, the PFR dependency graph, the *Proofs and Prompts* logo) are credited on the slides where they appear. The figures in the *Proofs and Prompts* slides come from the analysis in the repository root.

# Math 2.0: From Society to the Lab (slides)

Beamer project built on the Vidal lab template (`../vidal-lab-beamer`). Slides 2–3 have content; the rest hold working titles and grey planning notes. See `REFERENCE.md` for the talk's intent, structure, slide plan, facts and figure conventions.

## Build

```bash
latexmk main.tex
```

`.latexmkrc` selects XeLaTeX and writes to `build/`. The PDF is `build/main.pdf`.

## Layout

- `main.tex`: preamble, title slide, section order, and the time budget (45 min of content, 15 min of discussion).
- The talk is a tree mapped onto Beamer's levels: `\part` (Opening, Part I, Part II, Closing), then `\section` and `\subsection`. The "The rest of this talk" slide is generated from that tree with `\tableofcontents`, so it updates as the structure changes. Part names are set once in `main.tex` (`\partnameone`, `\partnametwo`).
- `sections/NN-*.tex`: one file per section or subsection, one frame per planned slide. The first digit gives the part: `0x` opening, `1x` Part I, `2x` Part II, `3x` closing, `99` backup. To reorder the talk, reorder the `\input` lines in `main.tex`.
- `\stub{minutes}{purpose}`: grey planning note on a slide. Set `\stubsfalse` in `main.tex` to hide them all.
- `\sectionslide{Part I}{Society}`: divider slide.

## Changes from the template

These apply only to the copies in this folder; `../vidal-lab-beamer` is untouched.

- `slide_formats/section_slide.tex` (new): divider slide on the pptx's "2_Divider Slide" background (`image4.jpg`). The title sits on the page's vertical centre, with the optional label hanging just above it.
- `beamerthemevidal.sty`: if "Open Sans" isn't installed as a system font, the theme falls back to the copy bundled with TeX Live. Overleaf uses the system font as before.
- `slide_formats/title_slide.tex`: rebuilt with TikZ positioning, following the pptx title slide's geometry: the text block is right-aligned against a white rule at half the slide width, starting 40% of the way down. It now shows a subtitle, and its spacing no longer depends on the title's length.
- `beamerthemevidal.sty`: added fonts and colours for subtitle, institute, date and footline; author is one size smaller (`\large`).
- `slide_formats/content_slide.tex`: rebuilt to follow the pptx content layout on the 16cm page. The title band, colour line, body start, margins and logo position are set once as lengths at the top of the file. The title band and footer are drawn at fixed positions with TikZ. The footer has a hairline from the left edge of the page to the logo, then one line of fields separated by short dividers: short author | short title | breadcrumb (part in Penn red › section › subsection) on the left, slide number | logo on the right. Footer text starts at the same left edge as the frame title. The author and title fields use `\author[...]` and `\title[...]` short forms.
- `beamerthemevidal.sty`: frame-title size (15pt) matches the pptx; the left text margin is 0.35cm (half the pptx inset) and the right is 0.70cm; the body shares its left edge with the title and footer.
- `\slidesources{...}` (in `content_slide.tex`): source credits in small grey type, running bottom to top in the strip right of the body. They are centred on the body height and wrap to a second line instead of running past it.
- `slide_formats/section_slide.tex`: `\sectionslide{}{Closing}` makes a divider with no label line.
- `slide_formats/content_slide.tex`: the footer is compressed to two lines of footer text (0.56 cm instead of 0.95 cm), with its text and a smaller Penn logo (0.42 cm tall) centred vertically in it. The body gains 0.39 cm.
- Only the template media actually used are copied: `image2.jpg` (title slide) and `image4.jpg` (divider).

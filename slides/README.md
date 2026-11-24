# Slides: Markdown → PDF

Workshop slides use **Marp Markdown**. Each file under `slides/decks/*.md` produces one **16:9 PDF presentation**.

## Create a slide deck

Copy [00-template.md](decks/00-template.md), for example to `decks/02-context-engineering.md`. Use `---` to separate slides.

- `#` = slide title
- `##` = subtitle
- `<!-- _class: lead -->` = dark title slide
- `<!-- _class: section -->` = colored section divider
- Standard Markdown for lists, tables, code, and quotations
- Live preview in VS Code using the **Marp for VS Code** extension

**PDF through GitHub:** A push changing `slides/**` automatically runs the PDF build. Download the `workshop-slides-pdf` artifact from **Actions → Build workshop slides → Artifacts**. You can also run the workflow manually.

**Local PDF build:** With Docker installed, run from the repository root:

```bash
bash scripts/build-slides.sh
```

The files appear in `slides/dist/*.pdf`. The official Marp CLI image provides Chromium, so no local Marp or browser installation is needed. Codespaces is intended for Markdown previews; the PDF build runs in GitHub Actions.

## Design

The minimal [TU Ilmenau slide theme](themes/tu-ilmenau.css) uses the university's documented colors:

| Role | Color |
|---|---|
| Dark blue | `#003359` |
| Green | `#00747A` |
| Orange accent | `#FF7900` |

**Color source:** *Technische Universität Ilmenau – Corporate Design*, “Die Farben,” pp. 6–7: [Corporate Design Manual (PDF)](https://www.designtagebuch.de/cd-manuals/TU-Ilmenau-Corporate_Design.pdf). The layout also follows the earlier minimal Markdown-to-PDF style, while using the documented color values.

The theme uses **Arial** or an open sans-serif fallback. It does not embed a university logo or proprietary university fonts and is not an officially approved university publication template.

## Implementation

- [Marp CLI](https://github.com/marp-team/marp-cli) for Markdown → PDF
- [scripts/build-slides.sh](../scripts/build-slides.sh) for local builds
- [GitHub Actions](../.github/workflows/build-slides.yml) for automated exports
- `slides/dist/` is excluded from Git

The source Markdown and theme CSS remain fully editable and version-controlled.

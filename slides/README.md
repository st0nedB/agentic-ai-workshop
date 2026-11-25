# Slides: Markdown → PDF

Workshop slides use **Marp Markdown**. Each file under `slides/decks/*.md` produces one **16:9 PDF presentation**.

## A4 handout

[Prompting cheat sheet (PDF)](handouts/prompting-cheat-sheet.pdf) is a one-page printable companion to Block 2. The workflow includes it in the workshop PDFs and uploads a separate `prompting-cheat-sheet` artifact. To update the checked-in PDF, install ReportLab and run `python3 slides/handouts/prompting-cheat-sheet.py` from the repository root.

## Create a slide deck

Copy [00-template.md](decks/00-template.md), for example to `decks/02-context-engineering.md`. Use `---` to separate slides.

- `#` = slide title
- `##` = subtitle
- `<!-- _class: lead -->` = dark title slide
- `<!-- _class: section -->` = colored section divider
- Standard Markdown for lists, tables, code, and quotations
- Live preview in VS Code using the **Marp for VS Code** extension

**PDF through GitHub:** A push changing `slides/**` on `main` automatically runs the PDF build. The `workshop-slides-pdf` Actions artifact remains available for build verification. You can also run the workflow manually.

## Publish a version

Only a pushed Git tag triggers release publication. The tag name is the workshop version; use a version such as `v1.0.0`. Tag the commit that contains the intended workshop materials:

```bash
git tag -a v1.0.0 -m "Workshop v1.0.0"
git push origin v1.0.0
```

GitHub Actions builds the PDFs from the tagged commit and publishes each PDF separately under [Releases](https://github.com/st0nedB/agentic-ai-workshop/releases), using the tag as the release title. The release contains individual PDF assets, not a ZIP of the slides. GitHub may additionally show its automatic source-code archives.

Ordinary branch pushes and manual workflow runs never publish releases. Existing release assets are not overwritten on retries. Create a new version tag for changed slides; do not move an existing tag.

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

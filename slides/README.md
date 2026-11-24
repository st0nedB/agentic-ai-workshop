# Folien: Markdown → PDF

Die Workshop-Folien werden als **Marp-Markdown** gepflegt. Eine Datei unter `slides/decks/*.md` ergibt genau eine PDF-Präsentation im **16:9-Format**.

## Neue Präsentation erstellen

Die Vorlage [00-vorlage.md](decks/00-vorlage.md) kopieren, beispielsweise nach `decks/01-llm-und-agenten.md`. Mit `---` werden Folien getrennt.

- `#` = Folientitel
- `##` = Untertitel
- `<!-- _class: lead -->` = dunkle Titelfolie
- `<!-- _class: section -->` = farbige Abschnittsfolie
- Normales Markdown für Listen, Tabellen, Code und Zitate
- Marp-Vorschau direkt in VS Code mit der installierten Erweiterung **Marp for VS Code**

**PDF auf GitHub:** Ein Push mit Änderungen an `slides/**` baut automatisch PDFs. Unter **Actions → Build workshop slides → Artifacts** liegt die Datei `workshop-slides-pdf` mit allen Präsentationen. Der Workflow kann auch manuell gestartet werden.

**PDF lokal:** Mit installiertem Docker/Podman-Docker-CLI vom Repository-Stamm aus:

```bash
bash scripts/build-slides.sh
```

Ergebnis: `slides/dist/*.pdf`. Der Export verwendet den offiziellen, Chromium-haltigen Marp-Container. Damit muss lokal weder Marp noch Chromium installiert werden. In GitHub Codespaces ist nur die **Markdown-Vorschau** vorgesehen; der PDF-Build erfolgt über GitHub Actions.

## Gestaltung

Ein gemeinsames, minimalistisches Template unter [themes/tu-ilmenau.css](themes/tu-ilmenau.css) verwendet die **dokumentierten TU-Hausfarben**:

| Rolle | Farbe |
|---|---|
| Technisches Blau (Primär) | `#003359` |
| Traditionelles Grün (Primär) | `#00747A` |
| Orange (Akzent) | `#FF7900` |

**Quelle der Farbwerte:** *Technische Universität Ilmenau – Corporate Design*, Kapitel „Die Farben“, S. 6–7: [Corporate-Design-Handbuch (PDF)](https://www.designtagebuch.de/cd-manuals/TU-Ilmenau-Corporate_Design.pdf). Das Design orientiert sich zugleich am bisherigen schlichten Markdown-PDF-Template (dunkle Überschriften, helle Flächen, sparsame Akzente), verwendet aber die offiziellen Farbwerte anstatt nur angenäherter Farbtöne.

Als Schrift nutzt es **Arial** bzw. eine freie Sans-Serif-Fallbackschrift. Die universitätseigene Schrift und das TU-Logo sind bewusst **nicht** eingebettet. Das Template ist eine eigene Workshop-Gestaltung und keine offizielle, freigegebene TU-Publikationsvorlage.

## Technische Umsetzung

- [Marp CLI](https://github.com/marp-team/marp-cli) für Markdown → PDF
- [scripts/build-slides.sh](../scripts/build-slides.sh) als einheitlicher Build-Aufruf
- [GitHub Actions](../.github/workflows/build-slides.yml) für automatischen PDF-Export
- `slides/dist/` bleibt aus Git ausgeschlossen

Folieninhalte und Design bleiben vollständig in Textdateien versionierbar.

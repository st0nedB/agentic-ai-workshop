# Praxis 01 – Bring Ordnung ins Chaos

**Block 1: Vom LLM zum KI-Agenten · 40 Minuten Gruppenarbeit**

## Situation

Ihr übernehmt ein Forschungsprojekt. Euer Vorgänger hat einen Ordner mit unsortierten Dokumenten, Tabellen, Bildern und Notizen hinterlassen. Dateinamen sind uneinheitlich und einige Dateien könnten Duplikate oder ältere Versionen sein.

## Euer Auftrag

> Analysiert den Ordner `01_dateichaos/arbeitsordner/` und organisiert die Dateien so, dass neue Projektmitglieder sich schnell zurechtfinden.

Nutzt einen der vorinstallierten Agenten (`codex`, `claude`, `goose` oder `pi`). Gebt zunächst nur diesen offenen Arbeitsauftrag. Beobachtet, welche Dateien der Agent tatsächlich untersucht, welche Werkzeuge er aufruft und welche Entscheidungen er selbst trifft.

**Zeitvorschlag:** 5 Minuten Orientierung, 20 Minuten Agentenarbeit, 10 Minuten Ergebnisprüfung, 5 Minuten Beobachtungen notieren.

## Gemeinsame Auswertung

- Welche Änderungen hat der Agent vorgenommen?
- Hat er Inhalte geprüft oder nur aus Dateinamen geschlossen?
- Wie ging er mit möglichen Duplikaten, widersprüchlichen Versionen und Unsicherheit um?
- Welche Entscheidungen würdet ihr nicht ungeprüft übernehmen?

## Ausgangsdaten

Die **45 vollständig fiktiven Beispieldateien (16,26 MB)** werden beim Erstellen des Codespace automatisch nach `01_dateichaos/arbeitsordner/` geladen. Falls sie fehlen:

```bash
python3 01_dateichaos/material_bereitstellen.py
```

Um die Ausgangslage **unter Verlust aller Änderungen im Arbeitsordner** wiederherzustellen:

```bash
python3 01_dateichaos/material_bereitstellen.py --reset
```

Die Dateien stammen unverändert aus dem Workshop [Using AI Agents for Reproducible Research](https://github.com/techczech/agents-for-reproducibility). Die Lizenz- und Urheberangaben stehen in [QUELLEN_UND_LIZENZ.md](QUELLEN_UND_LIZENZ.md).

**Wichtig:** Nur mit den fiktiven Beispieldaten arbeiten; keine echten vertraulichen oder personenbezogenen Unterlagen hochladen.

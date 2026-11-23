# KI-Workshop – GitHub Codespaces

Dieses Repository stellt eine **agentenunabhängige** Umgebung für den Workshop bereit. Ein KI-Agent, OpenRouter und API-Keys werden erst später eingerichtet.

## Für Teilnehmer

1. Melde dich bei GitHub mit deinem eigenen Konto an.
2. Öffne **[Workshop-Codespace starten](https://codespaces.new/st0nedB/agentic-ai-workshop)**.
3. Wähle nach Möglichkeit die kleinste Maschine (2 vCPU / 8 GB RAM) und erstelle deinen Codespace.
4. Nach dem Start öffnet sich VS Code im Browser. Eigene Dokumente kommen in `workspace/eingang/`, Ergebnisse in `workspace/ergebnisse/`.
5. Dateien können über den VS-Code-Dateiexplorer hoch- und heruntergeladen werden.

Jeder Teilnehmer erstellt einen **eigenen Codespace**. Die Arbeitsordner anderer Teilnehmer sind nicht zugänglich. Für einen lokalen VS-Code-Client oder den SSH-Zugang gelten die normalen GitHub-Codespaces-Anmeldeschritte.

### Kosten und Beenden

Der Codespace wird dem GitHub-Konto zugerechnet, unter dem er erstellt wurde (vorbehaltlich abweichender Organisations-Abrechnung). Beachte das verfügbare Codespaces-Freikontingent. Stoppe den Codespace nach dem Workshop unter https://github.com/codespaces. Gestoppte Codespaces verursachen keine laufenden Rechenkosten, gespeicherte Daten können aber weiterhin Speicherplatz belegen.

### Datenschutz

`workspace/` ist in `.gitignore` ausgeschlossen, damit persönliche Dokumente nicht versehentlich versioniert werden. **Dies ist keine Verschlüsselung oder Zugriffskontrolle.** Hochgeladene Dateien liegen in der GitHub-Cloud. Prüfe vor dem Upload, ob die Verarbeitung eigener Dokumente zulässig ist. Gib API-Keys niemals in Dateien ein, die du committen oder veröffentlichen könntest.

## Technische Basis

- VS Code im Browser über GitHub Codespaces
- Python 3.12 und Git aus dem Microsoft-Devcontainer-Image
- Arbeitsverzeichnisse: `workspace/eingang/` und `workspace/ergebnisse/`
- Keine vorinstallierten KI-Agenten und keine Modellanbindung

Die Umgebung wird durch `.devcontainer/devcontainer.json` konfiguriert. Sie setzt keine lokale Docker-Installation voraus. Für das Training können später zusätzliche Werkzeuge und Erweiterungen ergänzt werden.

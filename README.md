**# Werwolf Spielleiter App

**Version:** 1.0  
**Autor:** Felix  
**Jahr:** 2026  

Eine Desktop-App für Spielleiter des Werwolf-Spiels. Die App basiert auf **Python**, **Flask** und **PyWebView** und ermöglicht das Verwalten von Spieleinstellungen, das Starten eines Servers sowie einen Dark/Light Mode.

---

## Funktionen

- **Main Menu**
  - Starten des internen Spiel-Servers
  - Beenden der App
  - Zugriff auf die Einstellungen

- **Settings Menu**
  - Sprache auswählen (Deutsch / English)
  - Server-Port einstellen
  - Dark/Light Mode aktivieren
  - Einstellungen speichern (werden in `settings.json` abgelegt)

- **WebView Desktop-App**
  - Läuft als eigenständiges Desktop-Fenster
  - Flask-Server läuft im Hintergrund
  - Dynamisches Laden und Speichern von Einstellungen

---

## Installation

1. **Python 3.10+ installieren**  
   Stelle sicher, dass Python und `pip` installiert sind.

2. **Abhängigkeiten installieren**  

```bash
pip install flask pywebview

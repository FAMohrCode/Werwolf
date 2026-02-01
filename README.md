## *Werwolf Spielleiter*

**Version:** Alpha  
**Autor:** Felix, FAMohr  
**Jahr:** 2026  

---

Eine Desktop-App für Spielleiter des Werwolf-Spiels. Die App basiert auf **Python**, **Flask** und **PyWebView** und ermöglicht das Verwalten von Spieleinstellungen. Spieler sollen das Spiel beitreten können und ihre Rolle schnell und einfach übermittelt bekommen. Es soll einfach und schnell erweiterbar sein und immer was neues kommen. 

---

### Aktuelle Funktionen

- **Main Menu**
  - Starten des internen Spiel-Servers
  - Beenden der App
  - Zugriff auf die Einstellungen


- **Settings Menu**
  - Server-Port einstellen
  - Einstellungen speichern (werden in `settings.json` abgelegt)


- **Lobby**
  - QR-Code wird generiert
  - Spieler aus dem Netzwerk können beitreten
  - Die Spielerliste wird angezeigt


- **WebView Desktop-App**
  - Läuft als eigenständiges Desktop-Fenster
  - Flask-Server läuft im Hintergrund
  - Dynamisches Laden und Speichern von Einstellungen

---

### Installation

1. **Python 3.10+ installieren**  
   Stelle sicher, dass Python und `pip` installiert sind.

2. **Abhängigkeiten installieren**  

```bash
pip install flask pywebview
```
---

### Entwickler

- **Frontend**
  - Felix


- **Backend**
  - Felix

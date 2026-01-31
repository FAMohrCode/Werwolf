import threading
import webview
from flask import Flask, render_template, jsonify, request
import json
import os
import server

app = Flask(__name__, template_folder="ui", static_folder="ui")

window = None

SETTINGS_FILE = 'settings.json'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/settings-data")
def get_settings_data():
    settings = {"language": "de", "port": 5050, "theme": "light"}
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    return jsonify(settings)


@app.route("/start-server", methods=["POST"])
def start_server_route():
    threading.Thread(target=server.run_server, daemon=True).start()
    return jsonify({"status": "Server gestartet"})

@app.route('/save-settings', methods=['POST'])
def save_settings():
    data = request.get_json()  # JSON vom Frontend
    if not data:
        return jsonify({"message": "Keine Daten empfangen"}), 400

    # Optional: prüfen, dass alle Keys da sind
    required_keys = ['language', 'port', 'theme']
    for key in required_keys:
        if key not in data:
            return jsonify({"message": f"Fehlender Wert: {key}"}), 400

    # Speichern in JSON-Datei
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return jsonify({"message": "Einstellungen gespeichert!"})

@app.route("/exit", methods=["POST"])
def exit_app():
    # Schließt das WebView-Fenster
    def close_window():
        global window
        if window:
            window.destroy()  # richtiges Schließen
    threading.Thread(target=close_window).start()
    return jsonify({"status": "App wird geschlossen..."})

def run_flask():
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)

def start():
    global window
    threading.Thread(target=run_flask, daemon=True).start()
    window = webview.create_window(
        "Werwolf – Spielleiter",
        "http://127.0.0.1:5000/",
        width=900,
        height=600
    )
    webview.start(gui='qt')

if __name__ == "__main__":
    start()

import threading
import webview
from flask import Flask, render_template, jsonify
import server

app = Flask(__name__, template_folder="ui", static_folder="ui")

window = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/start-server", methods=["POST"])
def start_server_route():
    threading.Thread(target=server.run_server, daemon=True).start()
    return jsonify({"status": "Server gestartet"})

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

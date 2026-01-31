from flask import Flask, render_template
import os
import json

app = Flask(__name__, template_folder="web", static_folder="web")

SETTINGS_FILE = 'settings.json'

@app.route("/")
def index():
    return render_template("index.html")

def run_server():
    settings = {"language": "de", "port": 5050, "theme": "light"}
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    app.run(host="127.0.0.1", port=settings["port"])

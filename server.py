from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__, template_folder="web")
SETTINGS_FILE = 'settings.json'
USERDATA_FILE = "temp/userdatas.json"

# Hilfsfunktion: JSON laden
def load_userdata():
    if not os.path.exists(USERDATA_FILE):
        return {}
    with open(USERDATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

# Hilfsfunktion: JSON speichern
def save_userdata(data):
    os.makedirs(os.path.dirname(USERDATA_FILE), exist_ok=True)

    with open(USERDATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


@app.route("/save_nickname", methods=["POST"])
def save_nickname():
    data = request.get_json()
    nickname = data.get("nickname")

    if not nickname:
        return jsonify({"message": "Kein Nickname angegeben!"}), 400

    users = load_userdata()

    # Prüfen, ob Nickname schon existiert
    for user in users.values():
        if user["nickname"] == nickname:
            return jsonify({
                "message": f"Nickname '{nickname}' ist schon vergeben!"
            }), 409
    lobby()

    # Nickname ist frei → speichern
    user_id = str(len(users) + 1)
    users[user_id] = {"nickname": nickname}
    save_userdata(users)

    return jsonify({
        "message": f"Nickname '{nickname}' gespeichert!"
    })

@app.route("/api/lobby-users")
def lobby_users():
    try:
        with open("temp/userdatas.json", "r") as f:
            data = json.load(f)

        # 🧹 Spieler ohne gültigen Nickname entfernen
        clean_data = {
            uid: user
            for uid, user in data.items()
            if user.get("nickname") and user["nickname"].strip()
        }

        return jsonify(clean_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lobby")
def lobby():
    return render_template("lobby.html")

def run_server():
    settings = {"language": "de", "port": 5050, "theme": "light"}
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    app.run(host="0.0.0.0", port=settings["port"])

from flask import Flask, render_template

app = Flask(__name__, template_folder="web", static_folder="web")

@app.route("/")
def index():
    return render_template("index.html")

def run_server():
    app.run(host="127.0.0.1", port=5001)

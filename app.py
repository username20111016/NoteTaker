from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
FILENAME = "notes.json"

def load_notes():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_notes(notes):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)

@app.route("/")
def index():
    notes = load_notes()
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add():
    category = request.form["category"].capitalize()
    text = request.form["text"]

    notes = load_notes()
    if category not in notes:
        notes[category] = []

    note = {
        "id": len(notes[category]) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "text": text
    }
    notes[category].append(note)
    save_notes(notes)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

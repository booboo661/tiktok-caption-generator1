from flask import Flask, render_template, request
import random

app = Flask(__name__)

def load_phrases():
    with open("phrases.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        ideas = load_phrases()
        result = random.choice(ideas)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from ai_engine import ask_ai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["task"]
        response = ask_ai(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

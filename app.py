from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("inicial.html")

@app.route("/carros")
def carros():
    return render_template("carros.html")


if __name__ == "__main__":
    app.run(debug=True)
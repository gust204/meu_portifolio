from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("inicial.html")

@app.route("/masc")
def masc():
    return render_template("masc.html")

@app.route("/fem")
def fem():
    return render_template("fem.html")

@app.route("/lanc")
def lanc():
    return render_template("lanc.html")

@app.route("/prom")
def prom():
    return render_template("prom.html")


if __name__ == "__main__":
    app.run(debug=True)
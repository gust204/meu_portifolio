from flask import Flask, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)

app.secret_key = "dev"

DB_PATH = (Path(__file__).parent / "database.db").resolve()

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)  
    conn.row_factory = sqlite3.Row   
    return conn


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

@app.route("/esp")
def esp():
    return render_template("esp.html")

@app.route("/nike")
def nike():
    return render_template("nike.html")

@app.route("/adidas")
def adidas():
    return render_template("adidas.html")

@app.route("/puma")
def puma():
    return render_template("puma.html")

@app.route("/mormaii")
def mormaii():
    return render_template("mormaii.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/favoritos")
def favoritos():
    return render_template("favoritos.html")

@app.route("/bolsa")
def bolsa():
    return render_template("bolsa.html")


if __name__ == "__main__":
    app.run(debug=True)
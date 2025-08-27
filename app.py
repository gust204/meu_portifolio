from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)

app.secret_key = "dev"

DB_PATH = (Path(__file__).parent / "database.db").resolve()

DATABASE = "database.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not DB_PATH.exists():
        print("[INIT_DB] Criando novo banco...")
        with get_db_connection() as conn:
            conn.executescript("""
                CREATE TABLE usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    sobrenome TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    senha TEXT NOT NULL
                );
            """)
            conn.commit()
        print("[INIT_DB] Banco criado em:", DB_PATH)


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

@app.route("/add", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        email = request.form["email"]
        senha = request.form["senha"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES (?, ?, ?)",
            (nome, sobrenome, email, senha),
        )
        conn.commit()
        conn.close()
        return "Usuário cadastrado com sucesso!"
    
    return render_template("add.html")

@app.route("/favoritos")
def favoritos():
    return render_template("favoritos.html")

@app.route("/bolsa")
def bolsa():
    return render_template("bolsa.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/usuarios")
def listar_usuarios():
    db = get_db_connection()
    usuarios = db.execute("SELECT * FROM usuarios").fetchall()
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
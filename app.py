from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from pathlib import Path

app = Flask(__name__)
app.secret_key = "dev"

# ---- Config do banco (SQLite via SQLAlchemy) ----
DB_PATH = (Path(__file__).parent / "database.db").resolve()
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---- Modelo (tabela usuarios) ----
class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)  # guarda o hash

    def __repr__(self):
        return f"<Usuario {self.nome} {self.sobrenome}>"

# Cria as tabelas se não existirem
with app.app_context():
    db.create_all()

# ----------------- PÁGINAS PRINCIPAIS -----------------
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

@app.route("/favoritos")
def favoritos():
    return render_template("favoritos.html")

@app.route("/bolsa")
def bolsa():
    return render_template("bolsa.html")


# ----------------- CADASTRO -----------------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = (request.form.get("nome") or "").strip()
        sobrenome = (request.form.get("sobrenome") or "").strip()
        email = (request.form.get("email") or "").strip().lower()
        senha = (request.form.get("senha") or "").strip()

        if not (nome and sobrenome and email and senha):
            flash("Preencha todos os campos.", "error")
            return redirect(url_for("cadastro"))

        # hash da senha
        senha_hash = generate_password_hash(senha)

        novo = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=senha_hash)
        try:
            db.session.add(novo)
            db.session.commit()
            flash("Usuário cadastrado com sucesso! Faça login para continuar.", "success")
            return redirect(url_for("login"))
        except IntegrityError:
            db.session.rollback()
            flash("Este e-mail já está cadastrado.", "error")
            return redirect(url_for("cadastro"))
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao cadastrar: {e}", "error")
            return redirect(url_for("cadastro"))

    # GET: renderiza a sua página combinada (login+cadastro)
    return render_template("cadastro.html")


# ----------------- LOGIN / LOGOUT -----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        senha = (request.form.get("senha") or "").strip()

        user = Usuario.query.filter_by(email=email).first()
        if user and check_password_hash(user.senha, senha):
            session["usuario_id"] = user.id
            session["usuario_nome"] = user.nome
            flash(f"Bem-vindo(a), {user.nome}!", "success")
            return redirect(url_for("home"))
        else:
            flash("E-mail ou senha incorretos.", "error")
            return redirect(url_for("login"))

    # GET: usa o mesmo template onde já existe o bloco de login
    return render_template("cadastro.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da conta.", "info")
    return redirect(url_for("login"))


# ----------------- LISTAGEM (opcional p/ admin/teste) -----------------
@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.query.order_by(Usuario.id.desc()).all()
    return render_template("usuarios.html", usuarios=usuarios)


# ----------------- (Opcional) Proteção simples de rota -----------------
def login_obrigatorio(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get("usuario_id"):
            flash("Faça login para acessar.", "error")
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper

# Exemplo de uso:
# @app.route("/favoritos")
# @login_obrigatorio
# def favoritos():
#     return render_template("favoritos.html")


if __name__ == "__main__":
    app.run(debug=True)
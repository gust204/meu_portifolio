import sqlite3

# Cria/abre o banco
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Cria tabela "usuarios" (se não existir)
c.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
''')

conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute('''
CREATE TABLE cadastro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT UNIQUE NOT NULL
)
''')

conn.commit()

conn.close()
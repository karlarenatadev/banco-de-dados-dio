import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'cadastro.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)',
                    ('Karla Rosario', 'karla.rosario@email.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?)',
                    (2, 'Karla Rosario', 'karla.rosario@email.com'))
    conexao.commit()
except Exception as exc:
    print(f"Ops! Um erro ocorreu: {exc}")
    conexao.rollback()
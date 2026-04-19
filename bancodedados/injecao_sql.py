# contra vazamento de dados:
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'cadastro.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

id_cliente = input('Digite o ID do cliente: ')
cursor.execute('SELECT * FROM clientes WHERE id = ?', (id_cliente,)) # essa é a parte principal contra a injeção de SQL, o uso do '?' e a passagem do valor como tupla

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))
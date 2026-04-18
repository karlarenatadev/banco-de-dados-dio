import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'cadastro.db')
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        telefone VARCHAR(20) NOT NULL
    )''')

def inserir_dados(conexao, cursor, nome, email, telefone):
    data = (nome, email, telefone)
    cursor.execute('INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)', data)
    conexao.commit()

def inserir_dados_em_lote(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)', dados)
    conexao.commit()

def atualizar_dados(conexao, cursor, id, nome, email, telefone):
    data = (nome, email, telefone, id)
    cursor.execute('UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?', data)
    conexao.commit()

def excluir_dados(conexao, cursor, id):
    cursor.execute('DELETE FROM clientes WHERE id = ?', (id,))
    conexao.commit()

#   inserir_dados_em_lote(conexao, cursor, [
#       ('João Silva', 'joao.silva@email.com', '11999999999'),
#       ('Gabriela Souza', 'gabriela.souza@email.com', '11888888888'),
#       ('Marcos Oliveira', 'marcos.oliveira@email.com', '11777777777'),
#       ('Fernanda Costa', 'fernanda.costa@email.com', '11666666666'),
#       ('Ricardo Lima', 'ricardo.lima@email.com', '11555555555')
#    ])

def recuperar_dados(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?', (id,))
    return cursor.fetchone()

def listar_dados(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome DESC;')

clientes = listar_dados(cursor)
for cliente in clientes:
    print(cliente)

cliente = recuperar_dados(cursor, 2)
print(dict(cliente))

print(f'Seja bem-vindo, {cliente["nome"]}!')
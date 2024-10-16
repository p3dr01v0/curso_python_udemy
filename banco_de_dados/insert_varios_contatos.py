from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'insert into contatos (nome, telefone) values (%s, %s)'
args = (
    ('Bia', '18765-4321'),
    ('Jao', '28765-4322'),
    ('Lua', '38765-4323'),
    ('Gui', '48765-4324'),
    ('Ana', '58765-4325'),
    ('Beca', '68765-4326'),
    ('mrs', '78765-4327')
)

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            print(f'Foram incluidos {cursor.rowcount} registros')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

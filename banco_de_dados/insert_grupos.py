from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = "insert into grupos  (nome, descricao) values (%s, %s)"
args = (
    ('casa', 'grupo sobre a casa'),
    ('amigos', 'altas aventuras')
)

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.executemany(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro na CONEXÃO: {e.msg}')
        else:
            print(f'{cursor.rowcount} linhas afetadas')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

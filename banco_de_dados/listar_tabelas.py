from mysql.connector import ProgrammingError
from bd import nova_conexao

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute('show tables')

            for i, table in enumerate(cursor, start=1):
                print(f'Tabela {i}: table {table}')

        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO')

from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'select nome, telefone from contatos limit 10'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            print(f'{cursor.fetchone()}')
            print(f'{cursor.fetchone()}')
            print(f'{cursor.fetchone()}')
            print(f'{cursor.fetchone()}')
            print(f'{cursor.fetchone()}')
            print(f'{cursor.fetchone()}')
            print(f'{cursor.fetchone()}')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

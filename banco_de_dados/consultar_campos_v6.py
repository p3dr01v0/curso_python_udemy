from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'select nome from contatos order by nome desc'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            for x in cursor:
                print(f' '.join(x))
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

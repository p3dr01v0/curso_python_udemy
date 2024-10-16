from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'select * from contatos where telefone=\'98765-4321\' limit 10'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            for x in cursor.fetchall():
                print(x)
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

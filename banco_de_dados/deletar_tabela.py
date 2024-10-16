from bd import nova_conexao
from mysql.connector import ProgrammingError

deletar_emails = '''
    drop table emails
'''

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(deletar_emails)
        except ProgrammingError as e:
            print('erro ao executar', {e.msg})
except ProgrammingError as e:
    print('erro na Conexão', {e.msg})

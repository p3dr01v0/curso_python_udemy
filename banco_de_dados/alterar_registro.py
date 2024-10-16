from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'update contatos set nome=\'sol\' where nome = %s'
args = ('mrs',)

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro na CONEXÃO: {e.msg}')
        else:
            print(f'{cursor.rowcount} registros atualizados')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

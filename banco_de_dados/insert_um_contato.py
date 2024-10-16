from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'insert into contatos (nome, telefone) values (%s, %s)'
args = ('teste', '11111-2222')

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, args)
            conexao.commit()
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            print('sucesso ao adicionar ID:', cursor.lastrowid)
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

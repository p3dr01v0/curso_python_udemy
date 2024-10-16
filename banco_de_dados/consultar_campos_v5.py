from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'select * from contatos where nome like %s'

try:
    with nova_conexao() as conexao:
        try:
            nome = input('Contato a localizar: ')
            args = (f'%{nome}%', )

            cursor = conexao.cursor()
            cursor.execute(sql, args)
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            for x in cursor:
                print(x)
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

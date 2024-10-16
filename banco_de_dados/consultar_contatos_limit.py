from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'select * from contatos limit 5'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            contatos = cursor.fetchall()
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            for ctt in contatos:
                print(f'ID {ctt[2]:2d}, {ctt[0]:10s} telefone {ctt[1]}')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

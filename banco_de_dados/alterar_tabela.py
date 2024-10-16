from bd import nova_conexao
from mysql.connector import ProgrammingError

sql = 'alter table contatos add column id_contato int auto_increment primary key'

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

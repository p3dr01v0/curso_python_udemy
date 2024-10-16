from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_ctt = """
    create table if not exists contatos(
      nome varchar(225),
      telefone varchar(40)  
    );
"""

tabela_emails = """
    create table if not exists emails(
        id_email int auto_increment primary key,
        dono varchar(225)
    )
"""

with nova_conexao() as conexao:
    try:
        execucao = conexao.cursor()
        execucao.execute(tabela_ctt)
        execucao.execute(tabela_emails)
    except ProgrammingError as e:
        print('erro', {e.msg})

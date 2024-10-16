from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_grupo = """
    create table if not exists grupos(
        id_grupo int auto_increment primary key,
        descricao varchar(225)
    );
"""

alterar_contato_1 = """
    alter table contatos add grupo_id int
"""

alterar_contato_2 = """
    alter table contatos add foreign key (grupo_id) 
    references grupos (id_grupo)
"""

with nova_conexao() as conexao:
    try:
        execucao = conexao.cursor()
        execucao.execute(tabela_grupo)
        execucao.execute(alterar_contato_1)
        execucao.execute(alterar_contato_2)
    except ProgrammingError as e:
        print('erro', {e.msg})

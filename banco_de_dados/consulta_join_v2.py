from collections import defaultdict
from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = """
    select grupos.nome as grupo, contatos.nome as nome
    from contatos inner join grupos 
    on contatos.grupo_id = grupos.id_grupo
    order by grupo, nome
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor(dictionary=True)
            try:
                cursor.execute(sql)
                contatos = cursor.fetchall()
            finally:
                cursor.close()
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            agrupados = defaultdict(list)
            for contato in contatos:
                agrupados[contato['grupo']].append(contato['nome'])
                print(agrupados)

except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

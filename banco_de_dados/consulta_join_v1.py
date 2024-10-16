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
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            for consultas in cursor.fetchall():
                # print(f'\t'.join(str(campo) for campo in consultas))
                print(f'{consultas['grupo']}: {consultas['nome']}')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

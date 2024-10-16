from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

selecionar_grupo = 'select id_grupo from grupos where nome = %s'
atualizar_contatos = 'update contatos set grupo_id = %s where nome = %s'

contato_grupo = {
    'Lucas': 'amigos',
    'Bia': 'casa',
    'Jao': 'amigos',
    'Lua': 'amigos',
    'sol': 'amigos',
    'Ana': 'casa',
    'Beca': 'casa',
}

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            for contato, grupo in contato_grupo.items():
                cursor.execute(selecionar_grupo, (grupo,))
                grupo_id = cursor.fetchone()[0]
                cursor.execute(atualizar_contatos, (grupo_id, contato))
                conexao.commit()
        except ProgrammingError as e:
            print(f'Erro ao EXECUTAR: {e.msg}')
        else:
            print(f'contatos associados')
except ProgrammingError as e:
    print(f'Erro na CONEXÃO: {e.msg}')

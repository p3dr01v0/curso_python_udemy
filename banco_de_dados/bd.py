from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    user='root',
    port=3306,
    passwd='banco123',
    auth_plugin='mysql_native_password',
    database='agenda'
)


@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
            # print('finally...')

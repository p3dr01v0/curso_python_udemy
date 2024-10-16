from mysql.connector import connect

conexao = connect(
    host='localhost',
    user='root',
    port=3306,
    passwd='banco123',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()
cursor.execute('show databases')

for i, database in enumerate(cursor, start=1):
    print(f'banco de dados {i}, {database[0]}')

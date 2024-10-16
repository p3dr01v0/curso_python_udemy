from mysql.connector import connect

conexao = connect(
    host='localhost',
    user='root',
    port=3306,
    passwd='banco123',
    auth_plugin='mysql_native_password'
)

print(conexao)

import mysql.connector
def conexion (localhost, usuario, contra):
    conexion = mysql.connector.connect(
        host = localhost,
        user = usuario,
        password = contra,
        database = 'PRIMARK_SHOP'
    )
    return conexion

con = conexion('localhost', 'root', 'root')
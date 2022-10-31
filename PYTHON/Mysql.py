import mysql.connector

#Comprueba la conectividad a la instancia local



try:

    cnx = mysql.connector.connect(user='xXAnderJamesXx', password='AlexanderJC1810',

                            host='localhost',

                            database='PRIMARK_SHOP')

                              #auth_plugin='mysql_native_password')##host='127.0.0.1',database='employees')

    #with mysql.connector.connect(user='pruebasPython', password='Secret<>', host='LOCALHOST', database='pruebas1') as cnx:

    print("conexion exitosa!")

except:

    print("Fallo en la conexión")

finally:

    cnx.close()
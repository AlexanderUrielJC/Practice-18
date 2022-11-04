from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def home():
#Con render_template se utiliza para poder exportar y trabajar con un archivo html usando este Index como iniciador o arranque del sitio.
    return render_template('Myworld.html')
#El @ se utiliza para crear un modulo para la pagina web (crear URL del servidor)
#Utilizamos el metodo (route) nos dice que aqui podemos ponerle un nombre que se utilizara para 
#direccionarnos a otro apartado del URL por ejemplo 'localhost:5000/about' nos direccionara al acerca de. del sitio web
@app.route('/about')
#Defino la variable como tal 'about' y la defino en la variable como '/about' nombre que recibe el codigo que se utilizara para 
#direccionarnos a about de la pagina webcl
def about():
#Que como resultado saldra en pantalla el nombre de la pagina ?
    return render_template('about.html')
#Aqui validamos que el archivo es el que se esta trabajando como principal y es la que arranca la aplicacion
if __name__ == '__main__':
#Opcion 'debug' hace que le digamos al sistema que estamos haciendo cambios y que se actualice sin necesidad de estar reiniciando el server local
#valor buleando 'True' esta en modo de prueba
    app.run(debug=True)

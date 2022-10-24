import logging
from PyQt5 import QtWidgets, uic

#iniciar la aplicacion
app=QtWidgets.QApplication([])

#cargar la aplicacion
login= uic.loadUi("ventana1.ui")
entrar= uic.loadUi("ventana2.ui")
error= uic.loadUi("ventana3.ui")

def gui_login():
    name=login.txtUsuario.text()
    password= login.txtContrasena.text()
    if len(name)==0 or len(password)==0:
        login.label.setText("Ingrese todos los datos")
    elif name=="fabi" or password=="123":
        gui_entrar()
    else:
        gui_error()

def gui_entrar():
    login.hide()
    entrar.show()

def gui_error():
    login.hide()
    error.show()

def regresar_entrar():
    entrar.hide()
    login.show()

def regresar_error():
    error.hide()
    login.show()  

def salir():
    app.exit()
#botones
login.btnEntrar.clicked.connect(gui_login)
login.btnSalir.clicked.connect(salir)


entrar.btnRegresar.clicked.connect(regresar_entrar)
entrar.btnSalir.clicked.connect(salir)

error.btnSalir_2.clicked.connect(regresar_error)
error.btnSalir.clicked.connect(salir)


#ejecutable
login.show()
app.exec()
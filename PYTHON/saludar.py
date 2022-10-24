from json import load
import logging
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
#from imagen import
import imagen
#iniciar la aplicacionS
app=QtWidgets.QApplication([])

#cargar la aplicacion
login= uic.loadUi("saludo.ui")


class ventanaPrincipal(QMainWindow):
    def __init__(self,parent=None):
        super(ventanaPrincipal, self).__init__(parent)

        self.setWindowIcon(QIcon(":imagen/saludar.png"))
        self.setWindowFlags(Qt.WindowsCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSise(400,400)

        self.initUI()
    def initUi(self):
        label= QLabel(self)
        label.setGeometry(20,20,100,100)
        label.set.Pixmap(QPixmap(":imagen/saludar.png").scaled(100,100, Qt.KeepAspectRatio, Qt.smoothtransformation))

def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('saludar.png')
        label.setPixmap(pixmap)
 
        self.show()


def gui_login():
    imagen=("saludar.png")
    name=login.txtNombre.text()
    if len(name)==0 :
        login.txtMostrar.setText("Ingrese todos lod datos")
    elif name== "fabiola":
        login.txtMostrar.setText("Hola Fabiola :) !!!!")
        login.label


login.btnSaludar.clicked.connect(gui_login)


#ejecutable
login.show()
app.exec()
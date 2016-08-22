import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
sys.path.append('../Code')
import Calculator

class Ingresar(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ingresar()

    def ingresar(self):

        l1 = QLabel()
        l1.setText("User")
        l1.setAlignment(Qt.AlignLeft)
        
        l2 = QLabel()
        l2.setText("Password")

        
        
        self.setGeometry(200,200,210,220)
        self.setFixedSize(400,200)
        self.setWindowTitle("Ingresar")
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main= Ingresar()
    main.show()
    window = QtGui.QWidget()
    window.setWindowTitle("Practica01") 
    sys.exit(app.exec_())

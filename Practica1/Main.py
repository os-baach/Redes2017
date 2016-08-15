import sys
sys.path.append('../GUI')
import GUI
from PyQt4 import QtGui,QtCore
from PyQt4.QtCore import Qt 


def main():
    app = QtGui.QApplication(sys.argv)
    main = Calculadora()
    main.show()
    window = QtGui.QWidget()
    window.setWindowTitle("Practica1")
    sys.exit(app.exec_())

if __name__ == "__name__":
    main()

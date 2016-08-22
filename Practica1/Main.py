from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from GUI.GUI import Calculadora
def main():
    set_global()
    app = QtGui.QApplication(sys.argv)
    main= Calculadora()
    main.show()
    window = QtGui.QWidget()
    window.setWindowTitle("Calculadora") 
    sys.exit(app.exec_())

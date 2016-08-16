# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
#sys.path.append('../Constants')
#sys.path.append('../Code')
from Constants import * 
import Calculator
from Parser import *


class Calculadora(QtGui.QMainWindow):

    # Método constructor del GUI
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
            #VARIABLES PARA GUARDAR EL ARBOL DE SINTAXIS ABSTRACTO:
        self.numero1 = -1
        self.numero2 = -1
        self.resultado = 3.1416
        self.operador = ""
        self.presionado = False
        self.operando = False
        self.mostrar = 0

        self.calculadora()

    # Interfaz gráfica de la calculadora.
    def calculadora(self):

        self.line = QtGui.QLineEdit(self)
        self.line.move(5,20)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        self.line.resize(160,25)

        cero = QtGui.QPushButton("0",self)
        cero.move(10,180)
        cero.resize(35,30)

        uno = QtGui.QPushButton("1",self)
        uno.move(10,145)
        uno.resize(35,30)

        dos = QtGui.QPushButton("2",self)
        dos.move(50,145)
        dos.resize(35,30)

        tres = QtGui.QPushButton("3",self)
        tres.move(90,145)
        tres.resize(35,30)

        cuatro = QtGui.QPushButton("4",self)
        cuatro.move(10,110)
        cuatro.resize(35,30)

        cinco = QtGui.QPushButton("5",self)
        cinco.move(50,110)
        cinco.resize(35,30)

        seis = QtGui.QPushButton("6",self)
        seis.move(90,110)
        seis.resize(35,30)

        siete = QtGui.QPushButton("7",self)
        siete.move(10,75)
        siete.resize(35,30)

        ocho = QtGui.QPushButton("8",self)
        ocho.move(50,75)
        ocho.resize(35,30)

        nueve = QtGui.QPushButton("9",self)
        nueve.move(90,75)
        nueve.resize(35,30)

        mas = QtGui.QPushButton("+",self)
        mas.move(130,75)
        mas.resize(35,30)

        menos = QtGui.QPushButton("-",self)
        menos.move(130,110)
        menos.resize(35,30)

        igual = QtGui.QPushButton("=",self)
        igual.move(130,145)
        igual.resize(35,65)
        igual.clicked.connect(self.Igual)

        c = QtGui.QPushButton("c",self)
        c.move(90,180)
        c.resize(35,30)
        c.clicked.connect(self.C)

        punto = QtGui.QPushButton(".",self)
        punto.move(50,180)
        punto.resize(35,30)

        multiplicacion = QtGui.QPushButton("*",self)
        multiplicacion.move(170,75)
        multiplicacion.resize(35,30)

        division = QtGui.QPushButton("/",self)
        division.move(170,110)
        division.resize(35,30)

        modulo = QtGui.QPushButton("%",self)
        modulo.move(170,145)
        modulo.resize(35,30)

        potencia = QtGui.QPushButton("x^2",self)
        potencia.move(170,180)
        potencia.resize(35,30)
        
        numeros = [cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]

        operaciones = [c,punto,mas,menos,multiplicacion,division,modulo,potencia]

        for i in numeros:
            i.clicked.connect(self.Numeros)
        
        for i in operaciones[2:]:
            i.clicked.connect(self.Operaciones)

        self.setGeometry(300,300,210,220)
        self.setFixedSize(210,220)
        self.setWindowTitle("Calculadora")
        self.show()

        
    def Numeros(self,presion):
        sender = self.sender()
        if self.operando == False:
            if self.numero1 == -1:
                self.numero1 = int(sender.text())
            else:
                self.numero1 = (self.numero1*10) + int(sender.text())
            ponerNumero = str(self.numero1)
        else:
            if self.numero2 == -1:
                self.numero2 = int(sender.text())
                ultimo = self.numero2
            else:
                ultimo = int(sender.text())
                self.numero2 = (self.numero2*10) + ultimo
            self.presionado = True
            ponerNumero = str(self.numero2)
        if self.presionado == True:
            self.line.setText(self.line.text() + str(ultimo))
        else:
            self.line.setText(ponerNumero)
            
    
    def Operaciones(self,mostrar):
        sender = self.sender()
        if self.operando == False:
            self.operando = True
            mostrar += 1
            self.operador = sender.text()
            if self.operador == "x^2":
                self.operador = "^"                
            self.line.setText(self.line.text() + self.operador)
        
    def Igual(self,opera):
        mostrar = 0
        self.numero1 = int(self.numero1)
        self.numero2 = int(self.numero2)
        arbolSintactico = Parser(self)
        self.resultado = arbolSintactico.realiza_op()
        print(self.resultado)
        self.line.setText(str(self.resultado))
        self.operando = False
        self.presionado = False
        self.numero1 = -1
        self.numero2 = -1
        self.operador = ""

    def C(self):
        self.line.clear()
        self.operando = False
        self.presionado = False
        self.numero1 = -1
        self.numero2 = -1
        self.resultado = 3.1416
        self.operador = ""

def main():
    set_global()
    app = QtGui.QApplication(sys.argv)
    main= Calculadora()
    main.show()
    window = QtGui.QWidget()
    window.setWindowTitle("Calculadora") 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()        

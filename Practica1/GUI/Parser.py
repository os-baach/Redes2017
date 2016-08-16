# -*- coding: utf-8 -*-
from Calculator import Calculator
import sys
#sys.path.append('../Constants')
import Constants

class Parser:

    def __init__(self, arbol):
        self.arbol = arbol

    def realiza_op(self):
        c = Calculator()
        if self.arbol.operador == "+":
            return c.suma(self.arbol.numero1,self.arbol.numero2)
        if self.arbol.operador == "-":
            return c.resta(self.arbol.numero1,self.arbol.numero2)
        if self.arbol.operador == "*":
            return c.multiplica(self.arbol.numero1,self.arbol.numero2)
        if self.arbol.operador == "/":
            return c.divide(self.arbol.numero1,self.arbol.numero2)
        if self.arbol.operador == "%":
            return c.modulo(self.arbol.numero1,self.arbol.numero2)
        if self.arbol.operador == "^":
            return c.cuadrado(self.arbol.numero1,self.arbol.numero2)

            
        
  

#! /usr/bin/env python
# -*- coding: utf-8 -*-

######################################################
# PURPOSE:Interfaz grafica de un cliente en PyQt4    #
#                                                    #
# Vilchis Dominguez Miguel Alonso                    #
#       <mvilchis@ciencias.unam.mx>                  #
#                                                    #
# Notes: El alumno tiene que implementar la parte    #
#       comentada como TODO(Instalar python-qt)      #
#                                                    #
# Copyright   16-08-2015                             #
#                                                    #
# Distributed under terms of the MIT license.        #
#################################################### #
import sys, getopt
import os
sys.path.insert(0, '/')
sys.path.insert(0, './GUI')
sys.path.insert(0, './Constants')

from os import path
from PyQt4 import QtCore, QtGui
from principal import Ui_Chat

class mi_skype(QtGui.QMainWindow, Ui_Chat):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)


# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main(argv):
    #set_global()
    app = QtGui.QApplication(sys.argv)
    main = mi_skype()
    main.show()
    #main= mi_skype()
    #main.show()
    window = QtGui.QWidget()
    window.setWindowTitle("Chat")
    try:
        opts, args = getopt.getopt(argv, "l", ["local="])
    except getopt.GetoptError:
        print("Hola")
        #TODO lanzar exepcion
    if opts: #Si el usuario mandó alguna bandera
        local = True if '-l' in opts[0] else False
    else:
        local = False
    #TODO Llamar a su ventana de login
    sys.exit(app.exec_())


if __name__ == '__main__':
    main("")

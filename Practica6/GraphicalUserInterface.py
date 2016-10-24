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
from os import path
from PyQt4 import QtCore, QtGui
from GUI.principal import Ui_Chat
from Constants.Constants import *
from Channel.Channel import *
from Channel.ApiServer import *

class mi_skype(QtGui.QMainWindow, Ui_Chat):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)


# **************************************************
#  Definicion de la funcion principal
#**************************************************
def main(argv):
    app = QtGui.QApplication(sys.argv)
    if sys.argv.__len__() > 2:
        puerto = int(sys.argv[2])
        print "Mi puerto:",puerto
    elif sys.argv.__len__() > 1:
        puerto = DEFAULT_PORT_SERVER
        print "Mi puerto:",puerto
    if sys.argv.__len__() > 1 and ('-s' == sys.argv[1] or '-S' == sys.argv[1]):
        print("Servidor")
        escucha = MyApiServerForever(puerto)
        escucha.serve()
    elif sys.argv.__len__() > 1 and ('-sl' in sys.argv[1] or '-SL' in sys.argv[1] or '-sL' in sys.argv[1] or '-Sl' in sys.argv[1]):
        print("Servidor")
        escucha = MyApiServerForever(puerto,ip = DEFAULT_IP)
        escucha.serve()
    else:
        main = mi_skype()
        main.show()
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

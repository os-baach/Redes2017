# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import os
import sys, getopt
sys.path.insert(0, '../Constants')
sys.path.append('../Constants/')
from Channel.Channel import Channel
from Constants.Constants import *
import time
import threading
from threading import Thread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Chat(object):
    def setupUi(self, Chat):
        # Principio
        self.canal = None
        self.contacto = None
        # Hasta aqui
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(753, 489)
        self.stackedWidget = QtGui.QStackedWidget(Chat)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 741, 481))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.formLayoutWidget = QtGui.QWidget(self.page_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(400, 260, 321, 181))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.login = QtGui.QPushButton(self.formLayoutWidget)
        self.login.setObjectName(_fromUtf8("login"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.login)
        self.newuser = QtGui.QPushButton(self.formLayoutWidget)
        self.newuser.setObjectName(_fromUtf8("newuser"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.newuser)
        self.salir = QtGui.QPushButton(self.formLayoutWidget)
        self.salir.setObjectName(_fromUtf8("salir"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.salir)
        self.gridLayoutWidget = QtGui.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(350, 80, 381, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 16))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.user = QtGui.QLineEdit(self.gridLayoutWidget)
        self.user.setObjectName(_fromUtf8("user"))
        self.gridLayout.addWidget(self.user, 0, 2, 1, 1)
        self.password = QtGui.QLineEdit(self.gridLayoutWidget)
        self.password.setInputMask(_fromUtf8(""))
        self.password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(120, 16))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.page_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 321, 321))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.ip_server = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.ip_server.setObjectName(_fromUtf8("ip_server"))
        self.gridLayout_3.addWidget(self.ip_server, 4, 0, 2, 1)
        self.port_server = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.port_server.setObjectName(_fromUtf8("port_server"))
        self.gridLayout_3.addWidget(self.port_server, 8, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_11.setMinimumSize(QtCore.QSize(120, 16))
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_4.setMinimumSize(QtCore.QSize(120, 16))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 9, 0, 1, 1)
        self.my_port = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.my_port.setObjectName(_fromUtf8("my_port"))
        self.gridLayout_3.addWidget(self.my_port, 11, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_3.setMinimumSize(QtCore.QSize(120, 16))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_10.setMinimumSize(QtCore.QSize(120, 16))
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 7, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(100, 50, 161, 41))
        self.label_6.setMinimumSize(QtCore.QSize(120, 16))
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.user_3 = QtGui.QLabel(self.page_2)
        self.user_3.setGeometry(QtCore.QRect(470, 0, 188, 147))
        self.user_3.setMinimumSize(QtCore.QSize(120, 16))
        self.user_3.setScaledContents(False)
        self.user_3.setObjectName(_fromUtf8("user_3"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.page_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, 0, 741, 481))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_18.setMinimumSize(QtCore.QSize(120, 16))
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_3.addWidget(self.label_18)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setMinimumSize(QtCore.QSize(120, 16))
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.lista_usuarios = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.lista_usuarios.setObjectName(_fromUtf8("lista_usuarios"))
        self.verticalLayout_3.addWidget(self.lista_usuarios)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.salir_2 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.salir_2.setObjectName(_fromUtf8("salir_2"))
        self.verticalLayout_3.addWidget(self.salir_2)
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setMinimumSize(QtCore.QSize(120, 16))
        self.label_13.setScaledContents(False)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayoutWidget = QtGui.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_19.setMinimumSize(QtCore.QSize(120, 16))
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_2.addWidget(self.label_19)
        self.ventana_chat = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.ventana_chat.setReadOnly(True)
        self.ventana_chat.setObjectName(_fromUtf8("ventana_chat"))
        self.verticalLayout_2.addWidget(self.ventana_chat)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.entrada_texto = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.entrada_texto.setObjectName(_fromUtf8("entrada_texto"))
        self.horizontalLayout.addWidget(self.entrada_texto)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.llamar_contacto = QtGui.QPushButton(self.verticalLayoutWidget)
        self.llamar_contacto.setObjectName(_fromUtf8("llamar_contacto"))
        self.horizontalLayout_2.addWidget(self.llamar_contacto)
        self.terminar_conversacion = QtGui.QPushButton(self.verticalLayoutWidget)
        self.terminar_conversacion.setObjectName(_fromUtf8("terminar_conversacion"))
        self.horizontalLayout_2.addWidget(self.terminar_conversacion)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_20.setMinimumSize(QtCore.QSize(120, 16))
        self.label_20.setScaledContents(False)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_2.addWidget(self.label_20)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.page_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 40, 551, 371))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setTextFormat(QtCore.Qt.PlainText)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout.addWidget(self.label_12)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.regresar_chat = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.regresar_chat.setObjectName(_fromUtf8("regresar_chat"))
        self.horizontalLayout_5.addWidget(self.regresar_chat)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.page_3)
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.page_5)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(190, 20, 371, 401))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.newuser_3 = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.newuser_3.setObjectName(_fromUtf8("newuser_3"))
        self.gridLayout_4.addWidget(self.newuser_3, 12, 0, 1, 1)
        self.new_password = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.new_password.setObjectName(_fromUtf8("new_password"))
        self.gridLayout_4.addWidget(self.new_password, 6, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_4.addWidget(self.label_14, 7, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_4.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_17.setMinimumSize(QtCore.QSize(120, 16))
        self.label_17.setScaledContents(False)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 11, 0, 1, 1)
        self.new_username = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.new_username.setObjectName(_fromUtf8("new_username"))
        self.gridLayout_4.addWidget(self.new_username, 3, 0, 2, 1)
        self.my_port_2 = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.my_port_2.setObjectName(_fromUtf8("my_port_2"))
        self.gridLayout_4.addWidget(self.my_port_2, 8, 0, 1, 1)
        self.newuser_2 = QtGui.QPushButton(self.gridLayoutWidget_4)
        self.newuser_2.setObjectName(_fromUtf8("newuser_2"))
        self.gridLayout_4.addWidget(self.newuser_2, 10, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 9, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)

        # Agregue estas dos instrucciones:
        self.entrada_texto.returnPressed.connect(self.enviar_msg)
        self.lista_usuarios.itemDoubleClicked.connect(self.inicia_conversacion)
        # Fin de las dos instrucciones.
        
        self.retranslateUi(Chat)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    # Aqui comienzan las funciones que yo defino en la GUI:

    # Nos inicia la sesion
    def iniciar_sesion(self, my_port):
        mi_puerto_str = str(self.my_port.text()).replace(" ","")
        mi_puerto = DEFAULT_PORT
        if self.num(mi_puerto_str):
            mi_puerto = int(mi_puerto_str)
        port_server_str = str(self.port_server.text()).replace(" ","")
        port_server = DEFAULT_PORT_SERVER
        if self.num(port_server_str):
            port_server = int(port_server_str)
        ip_server_str = str(self.ip_server.text()).replace(" ","")
        if ip_server_str == "":
            ip_server_str = DEFAULT_IP
        nombre_usuario = str(self.user.text()).replace(" ","")
        contrasenia = str(self.password.text())
        if not self.verificar(nombre_usuario,contrasenia):
            print("No está en la base de datos")
        else:
            self.canal = Channel(mi_puerto,port_server,self,ip_server_str,nombre_usuario)
            item = QListWidgetItem(nombre_usuario)
            self.lista_usuarios.addItem(item)
            self.empieza_refresh()
            print("OK")
            self.mover_pagina(1)
            
    # Funcion que busca que un usuario con su contraenia esten en
    # la base de datos.
    def verificar(self, nombre, contr):
        data = open(ARCHIVO,'r+')
        secret = ""
        for i in contr:
            secret = secret+chr(ord(i)+5)
        looking_for = nombre+":"+secret
        linea = data.readline()
        while linea:
            if linea == looking_for:
                return True
            else:
                linea = data.readline()
        return False
            
    def inicia_conversacion(self, item):    
        self.plainTextEdit.clear()
        txt = str(item.text())
        txt2 = txt.split('    Estado:')
        text = txt2[0]
        self.canal.set_temp(text)
        self.__next_page()
        self.canal.comienza_conver(text)

    def disponible(self,key):
        return self.canal.get_status(key)

    def enviar_msg(self):
        mensaje = self.entrada_texto.text()
        self.canal.send_text("%s" % mensaje)
        time.sleep(0.25)
        self.plainTextEdit.insertPlainText("Yo: "+mensaje+"\n")
        self.plainTextEdit.insertPlainText("\n")
        self.entrada_texto.clear()        

    def exit_fun(self):
        sys.exit()
        
    def salir_fun(self):
        self.canal.log_out()
        sys.exit()
        
    def num(self,n):
        try:
            if str(n).replace(" ","") == "":
                return False            
            int(n)
            return True
        except ValueError:
            return False

    def regresar_chat_fun(self):
        self.mover_pagina(2)
        self.colgar()

    def mover_pagina(self,pag):
        if pag < self.stackedWidget.count()-1:
            self.stackedWidget.setCurrentIndex(pag)

    def conectar_server(self):
        self.mover_pagina(1)
        
    """
    def __next_page(self):
        idx = self.stackedWidget.currentIndex()
        if idx == 1:
            self.stackedWidget.setCurrentIndex(idx + 1)
            return idx+1
        if idx < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(idx + 1)
        else:
            self.stackedWidget.setCurrentIndex(0)
            

    def __previous_page(self):
        idx = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(idx-1)   """

    def llamar(self):
        idx = self.stackedWidget.currentIndex()
        if idx < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(idx + 1)
        else:
            self.stackedWidget.setCurrentIndex(1)
        self.canal.llamar()
        self.canal.videollamar()
        
    def colgar(self):
        self.canal.colgar()
        

    # Funcion que tira un thread para actualizar la lista.
    def empieza_refresh(self):
        self.refreshThread = Thread(target=self.actualizar_lista)
        self.refreshThread.daemon = True
        self.refreshThread.start()
        
    # Funcion que actualiza la lista de usuarios constantemente
    def actualizar_lista(self):
        tam = self.canal.get_nombres()
        varIt = 0
        while True:
            lock = threading.Lock()
            lock.acquire()
            nombres = self.canal.get_nombres()
            if tam != len(nombres) or varIt > 5:
                varIt = 0
                self.lista_usuarios.clear()
                tam = len(nombres)
                for key, value in nombres.iteritems():
                    self.lista_usuarios.addItem(key+"    Estado: "+self.disponible(key))
            lock.release()
            varIt = varIt + 1
            time.sleep(0.5)


    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "Chat", None))
        self.login.setText(_translate("Chat", "   Login   ", None))
        self.newuser.setText(_translate("Chat", "Registrar", None))
        self.salir.setText(_translate("Chat", "    Salir    ", None))
        self.label_2.setText(_translate("Chat", "Nombre de usuario:", None))
        self.user.setPlaceholderText(_translate("Chat", "Usuario", None))
        self.password.setPlaceholderText(_translate("Chat", "Contraseña", None))
        self.label_5.setText(_translate("Chat", "Contraseña:", None))
        self.ip_server.setPlaceholderText(_translate("Chat", "Ej: 192.168.33.1", None))
        self.port_server.setPlaceholderText(_translate("Chat", "Ej: 5000", None))
        self.label_11.setText(_translate("Chat", "Default: 5000 ", None))
        self.label_4.setText(_translate("Chat", " ¿Cuál es la dirección ip del servidor de contacto?", None))
        self.label_9.setText(_translate("Chat", "Opcional: ¿Cuál es tu puerto?", None))
        self.my_port.setPlaceholderText(_translate("Chat", "Ej: 5000", None))
        self.label_8.setText(_translate("Chat", "¿Cuál es el puerto del servidor? ", None))
        self.label_3.setText(_translate("Chat", "Default: localhost", None))
        self.label_10.setText(_translate("Chat", "Default: 5001", None))
        self.label_6.setText(_translate("Chat", "DATOS DE CONEXIÓN:", None))
        self.user_3.setText(_translate("Chat", "DATOS DEL USUARIO:", None))
        self.label_18.setText(_translate("Chat", " ", None))
        self.label_7.setText(_translate("Chat", "Da doble click sobre algún usuario que se encuentre \"Disponible\" para iniciar una conversación", None))
        self.salir_2.setText(_translate("Chat", "Salir", None))
        self.label_13.setText(_translate("Chat", " ", None))
        self.label_19.setText(_translate("Chat", "  ", None))
        self.label.setText(_translate("Chat", "Ingresar\n"
" texto:", None))
        self.entrada_texto.setPlaceholderText(_translate("Chat", "[Escribe aquí el texto]", None))
        self.llamar_contacto.setText(_translate("Chat", "Llamar a contacto", None))
        self.terminar_conversacion.setText(_translate("Chat", "Terminar conversación", None))
        self.label_20.setText(_translate("Chat", "  ", None))
        self.label_12.setText(_translate("Chat", "VIDEOLLAMADA EN CURSO", None))
        self.regresar_chat.setText(_translate("Chat", "Regresar al chat", None))
        self.newuser_3.setText(_translate("Chat", "Cancelar y regresar", None))
        self.new_password.setPlaceholderText(_translate("Chat", "Password", None))
        self.label_14.setText(_translate("Chat", "Repetir contraseña:", None))
        self.label_15.setText(_translate("Chat", "Contraseña:", None))
        self.label_17.setText(_translate("Chat", "Nombre de usuario:", None))
        self.new_username.setPlaceholderText(_translate("Chat", "Ej: yo123", None))
        self.my_port_2.setPlaceholderText(_translate("Chat", "Password", None))
        self.newuser_2.setText(_translate("Chat", "Registrar", None))
        #Funciones de comportamiento:
        #Funciones de salida:
        self.salir.clicked.connect(self.exit_fun)
        self.salir_2.clicked.connect(self.salir_fun)
        
        #Funcion para colgar la videollamara:
        self.regresar_chat.clicked.connect(self.regresar_chat_fun)
        #Funcion para llamar a usuario:
        self.llamar_contacto.clicked.connect(self.llamar)
        #Funcion para iniciar sesion:
        #self.login.clicked.connect(self.iniciar_sesion)
        self.login.clicked.connect(self.exit_fun)
        #Funcion para regresar de la llamada al chat:
        self.regresar_chat.clicked.connect(self.regresar_chat_fun)
        #Funcion para termianar una conversacion:
        self.terminar_conversacion.clicked.connect(self.conectar_server)
        #self.pushButton_2.clicked.connect(self.__next_page)


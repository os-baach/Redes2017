# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
import sys, getopt
sys.path.insert(0, '../Constants')
sys.path.append('../Constants/')
from Channel.Channel import Channel
from Constants.Constants import MENSAJE_VISTA
from Constants.Constants import DEFAULT_PORT
from Constants.Singleton import *
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
        #Principio
        self.canal = None
        self.contacto = None
        #Hasta aqui
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(753, 489)
        self.stackedWidget = QtGui.QStackedWidget(Chat)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 741, 481))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.formLayoutWidget = QtGui.QWidget(self.page_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(400, 330, 321, 151))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formLayout_2.setLayout(5, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.pushButton = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        self.gridLayoutWidget = QtGui.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 211))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(120, 16))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.page_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 381, 241))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtGui.QWidget(self.page_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(400, 160, 321, 91))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 0, 2, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_4.setMinimumSize(QtCore.QSize(120, 16))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 2, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.page_4)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(-1, 0, 741, 481))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_3.addWidget(self.listWidget)
        #self.entrar_chat = QtGui.QPushButton(self.verticalLayoutWidget_3)
        #self.entrar_chat.setObjectName(_fromUtf8("entrar_chat"))
        #self.verticalLayout_3.addWidget(self.entrar_chat)
        #self.contacto_nuevo = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        #self.contacto_nuevo.setObjectName(_fromUtf8("contacto_nuevo"))
        #self.verticalLayout_3.addWidget(self.contacto_nuevo)
        #self.agregar_contacto = QtGui.QPushButton(self.verticalLayoutWidget_3)
        #self.agregar_contacto.setObjectName(_fromUtf8("agregar_contacto"))
        #self.verticalLayout_3.addWidget(self.agregar_contacto)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.salir_programa = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.salir_programa.setObjectName(_fromUtf8("salir_programa"))
        self.verticalLayout_3.addWidget(self.salir_programa)
        self.stackedWidget.addWidget(self.page_4)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayoutWidget = QtGui.QWidget(self.page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 481))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_2.addWidget(self.plainTextEdit)
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
        self.regresar = QtGui.QPushButton(self.verticalLayoutWidget)
        self.regresar.setObjectName(_fromUtf8("regresar"))
        self.horizontalLayout_2.addWidget(self.regresar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.page_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 40, 551, 371))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.plainTextEdit_2.setTabStopWidth(90)
        self.plainTextEdit_2.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.verticalLayout.addWidget(self.plainTextEdit_2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_5 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.page_3)

        self.entrada_texto.returnPressed.connect(self.enviar_msg)
        self.listWidget.itemDoubleClicked.connect(self.inicia_conversacion)
        
        self.retranslateUi(Chat)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Chat)


    def conectar(self, my_port):
        mi_puerto = my_port
        mi_nombre_usuario = str(self.lineEdit_2.text())
        su_puerto = self.lineEdit_3.text()
        ip_server = str(self.lineEdit_4.text()).replace(" ","")
        if not self.num(su_puerto):
            su_puerto = DEFAULT_PORT
        if ip_server != "":
            self.canal = Channel(int(str(mi_puerto)),int(str(su_puerto)),self,ip_server,mi_nombre_usuario)
        else:
            self.canal = Channel(int(str(mi_puerto)),int(str(su_puerto)),self,'127.0.0.1',mi_nombre_usuario)
        item = QListWidgetItem(mi_nombre_usuario)
        self.listWidget.addItem(item)
        self.empieza_refresh()

    def empieza_refresh(self):
        self.refreshThread = Thread(target=self.actualizar_lista)
        self.refreshThread.daemon = True
        self.refreshThread.start()
        
    def inicia_conversacion(self, item):
        #Temporal: Aqui va la conexion de un usuario con otro.
        self.plainTextEdit.clear()
        txt = str(item.text())
        txt2 = txt.split('    Estado:')
        text = txt2[0]
        self.canal.set_temp(text)
        self.__next_page()
        self.canal.comienza_conver(text)
        
        """def agrega_contacto(self):
        item = QListWidgetItem(self.contacto_nuevo.text())
        self.listWidget.addItem(item)
        self.contacto_nuevo.clear()"""

    def actualizar_lista(self):
        tam = self.canal.get_nombres()
        varIt = 0
        while True:
            lock = threading.Lock()
            lock.acquire()
            nombres = self.canal.get_nombres()
            if tam != len(nombres) or varIt > 5:
                varIt = 0
                self.listWidget.clear()
                tam = len(nombres)
                for key, value in nombres.iteritems():
                    self.listWidget.addItem(key+"    Estado: "+self.disponible(key))
            lock.release()
            varIt = varIt + 1
            time.sleep(0.5)

    def disponible(self,key):
        return self.canal.get_status(key)

    def enviar_msg(self):
        mensaje = self.entrada_texto.text()
        self.canal.send_text("%s" % mensaje)
        time.sleep(0.25)
        self.plainTextEdit.insertPlainText("Yo: "+mensaje+"\n")
        self.plainTextEdit.insertPlainText("\n")
        self.entrada_texto.clear()        
        
    def salir(self):
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

   # def worker(self):
   #     while True:
   #         global MENSAJE_VISTA
   #         if not MENSAJE_VISTA.get() == None:
   #             print(MENSAJE_VISTA.get())
   #             self.plainTextEdit.insertPlainText(MENSAJE_VISTA.get())
   #             time.sleep(1)
   #             MENSAJE_VISTA = OnlyOne(None)        
        
    def __next_page(self):
        idx = self.stackedWidget.currentIndex()
        if idx == 1:
            self.stackedWidget.setCurrentIndex(idx + 1)
            return idx+1
        var = False
        LOCAL = 5000
        while not var:            
            try:
                self.conectar(LOCAL)
                var = True
            except:
                LOCAL = LOCAL+1
                self.conectar(LOCAL)
                var = True
        if idx < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(idx + 1)
        else:
            self.stackedWidget.setCurrentIndex(0)
            

    def __previous_page(self):
        idx = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(idx-1)
        
    def regresar_chat(self):
        idx = self.stackedWidget.currentIndex()
        if idx < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(idx - 1)
        else:
            self.stackedWidget.setCurrentIndex(1)
        self.colgar()
            
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


        
    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "Chat", None))
        self.pushButton.setText(_translate("Chat", "Salir", None))
        self.pushButton_2.setText(_translate("Chat", "Aceptar", None))
        self.label_2.setText(_translate("Chat", "Nombre de usuario:                     ", None))
        self.label_3.setText(_translate("Chat", "¿Cuál es el puerto del servidor?", None))
        self.label_4.setText(_translate("Chat", " ¿Cuál es la dirección ip del servidor de contacto?", None))
        #self.entrar_chat.setText(_translate("Chat", "Actualizar lista conectados", None))
        #self.contacto_nuevo.setPlaceholderText(_translate("Chat", "[Ingresa el nombre del usuario que deseas agregar]", None))
        #self.agregar_contacto.setText(_translate("Chat", "Agregar contacto", None))
        self.salir_programa.setText(_translate("Chat", "Salir", None))
        self.label.setText(_translate("Chat", "Ingresar\n"
" texto:", None))
        self.entrada_texto.setPlaceholderText(_translate("Chat", "[Escribe aquí el texto]", None))
        self.llamar_contacto.setText(_translate("Chat", "Llamar a contacto", None))
        self.regresar.setText(_translate("Chat", "Regresar", None))
        self.plainTextEdit_2.setPlainText(_translate("Chat", "LLAMADA EN CURSO", None))
        self.pushButton_5.setText(_translate("Chat", "Regresar al chat", None))
        self.pushButton_4.setText(_translate("Chat", "Salir", None))
        #Funciones de comportamiento:
        #self.agregar_contacto.clicked.connect(self.agrega_contacto)
        self.pushButton_4.clicked.connect(self.salir)
        self.pushButton_5.clicked.connect(self.regresar_chat)
        self.llamar_contacto.clicked.connect(self.llamar)
        #self.entrar_chat.clicked.connect(self.actualizar_lista)
        self.salir_programa.clicked.connect(self.salir)
        self.pushButton.clicked.connect(self.salir)
        self.regresar.clicked.connect(self.__previous_page)
        self.pushButton_2.clicked.connect(self.__next_page)


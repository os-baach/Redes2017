# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, getopt
sys.path.insert(0, '../Constants')
sys.path.append('../Constants/')
from Channel.Channel import Channel
from Constants.Constants import MENSAJE_VISTA
from Constants.Constants import DEFAULT_PORT
from Constants.Singleton import *
import time
import threading

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
        self.canal = None        
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(741, 485)
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
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(430, 160, 291, 91))
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
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.formLayoutWidget.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.label_3.raise_()
        self.label_3.raise_()
        self.gridLayoutWidget_3.raise_()
        self.stackedWidget.addWidget(self.page_2)
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
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit.returnPressed.connect(self.enviar_msg)        
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Salir = QtGui.QPushButton(self.verticalLayoutWidget)
        self.Salir.setObjectName(_fromUtf8("Salir"))
        self.horizontalLayout_2.addWidget(self.Salir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget.raise_()
        self.plainTextEdit.raise_()
        self.stackedWidget.addWidget(self.page)

        self.retranslateUi(Chat)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Chat)
        
    def enviar_msg(self):
        mensaje = self.lineEdit.text()
        self.canal.send_text("%s" % mensaje)
        time.sleep(0.5)
        self.plainTextEdit.insertPlainText("Yo: "+mensaje+"\n")
        self.plainTextEdit.insertPlainText("\n")
        self.lineEdit.clear()
        
    def salir(self):
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
        mi_puerto = self.lineEdit_2.text()
        su_puerto = self.lineEdit_3.text()
        su_ip = str(self.lineEdit_4.text()).replace(" ","")
        if not self.num(mi_puerto):
            mi_puerto = DEFAULT_PORT
        if not self.num(su_puerto):
            su_puerto = DEFAULT_PORT
        if su_ip == "":
            self.canal = Channel(int(str(mi_puerto)),int(str(su_puerto)),self,su_ip)
        else:
            self.canal = Channel(int(str(mi_puerto)),int(str(su_puerto)),self)
        idx = self.stackedWidget.currentIndex()
        if idx < self.stackedWidget.count() - 1:
            self.stackedWidget.setCurrentIndex(idx + 1)
        else:
            self.stackedWidget.setCurrentIndex(0)
        #t = threading.Thread(target=self.worker)
        #t.start()        

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "Chat", None))
        self.pushButton.setText(_translate("Chat", "Salir", None))
        self.pushButton_2.setText(_translate("Chat", "Aceptar", None))
        self.label_2.setText(_translate("Chat", "¿Cuál es mi puerto?                     ", None))
        self.label_3.setText(_translate("Chat", "¿Cuál es el puerto del contacto?", None))
        self.label_4.setText(_translate("Chat", "Opcional: ¿Dirección ip del contacto?", None))
        self.label.setText(_translate("Chat", "Ingresar\n"
" texto:", None))
        self.lineEdit.setPlaceholderText(_translate("Chat", "[Escribe aquí el texto]", None))
        self.Salir.setText(_translate("Chat", "Salir", None))
        self.pushButton.clicked.connect(self.salir)
        self.Salir.clicked.connect(self.salir)
        self.pushButton_2.clicked.connect(self.__next_page)

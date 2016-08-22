# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append('../Channel/')
from PyQt4 import QtCore, QtGui
from Channel import Channel
 
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
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(580, 434)
        self.buttonBox = QtGui.QDialogButtonBox(Chat)
        self.buttonBox.setGeometry(QtCore.QRect(230, 400, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Chat)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 551, 351))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.lineEdit = QtGui.QLineEdit(Chat)
        self.lineEdit.setGeometry(QtCore.QRect(70, 370, 471, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Chat)
        self.label.setGeometry(QtCore.QRect(10, 370, 91, 31))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Chat)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Chat.accept)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Chat.reject)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "Chat", None))
        self.lineEdit.setPlaceholderText(_translate("Chat", "[Escribe aquí el texto]", None))
        self.label.setText(_translate("Chat", "Ingresar\n"
" texto:", None))
        # Crea el canal de comunicación(?)
        #canal = Channel()
        # Creo que así se le asigna una función a un botón:
        #self.buttonBox.clicked.connect(canal.send_text, args=('hola_rick'))
        


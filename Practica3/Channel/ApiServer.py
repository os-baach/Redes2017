#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket

sys.path.append('../Constants/')
import SimpleXMLRPCServer
from Constants.Constants import DEFAULT_PORT
from Constants.Constants import MENSAJE_VISTA
from Constants.Singleton import *


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip

class MyApiServer:
    def __init__(self,interfaz = None, con_local = False, my_port = DEFAULT_PORT):
        # Se crea un servidor en localhost:
        self.interfaz = interfaz
        if not con_local:
            my_ip = str(get_local_ip())
        else:
            my_ip = "127.0.0.1"
        print(my_ip)
        self.server = SimpleXMLRPCServer.SimpleXMLRPCServer((my_ip, my_port), allow_none = True)
        # Se registran las funciones del FunctionWrapper en el servidor:
        self.server.register_instance(FunctionWrapper(self.interfaz))
       
    # Inicializamos el servidor
    def serve(self):
        self.server.serve_forever()
        
class FunctionWrapper:
    def __init__(self,interfaz):
        # No estoy seguro de que haya algo que inicializar:
        self.interfaz = interfaz
        pass

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        # Regresamos el mensaje pa' que lo agarre el servidor:
        self.interfaz.plainTextEdit.insertPlainText("Contacto: "+message+ "\n")
        self.interfaz.plainTextEdit.insertPlainText("\n")
        print message




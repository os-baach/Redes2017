#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../Constants/')
import SimpleXMLRPCServer as serv
from Constants import DEFAULT_PORT

class MyApiServer:
    def __init__(self, my_port = DEFAULT_PORT):
        # Se crea un servidor en localhost:
        self.server = serv.SimpleXMLRPCServer(("localhost", my_port))
        # Se registran las funciones del FunctionWrapper en el servidor:
        self.server.register_instance(FunctionWrapper())
        # Creo que es necesario que el servidor no pare:
        self.server.serve_forever()
        
class FunctionWrapper:
    def __init__(self):
        # No estoy seguro de que haya algo que inicializar:
        pass

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        # Regresamos el mensaje pa' que lo agarre el servidor:
        return message




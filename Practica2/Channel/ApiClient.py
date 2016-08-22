#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../Constants/')
import xmlrpclib
from Constants import DEFAULT_PORT

class MyApiClient:

    def __init__(self, my_port = DEFAULT_PORT):
        # El servidor que nos mandará el texto:
        self.server = xmlrpclib.Server('http://localhost:' + str(my_port))

    # Muestra el texto recibido
    def muestra_texto(self, texto):
        # Espero esto sea lo que hay que hacer:
        print self.server.sendMessage_wrapper(texto)

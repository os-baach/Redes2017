#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib

class MyApiClient:

    def __init__(self, my_port = Constants.DEFAULT_PORT):
        # El servidor que nos mandará el texto:
        self.server = xmlrpclib.Server('http://localhost:' + str(my_port))

    def muestra_texto(self):
        

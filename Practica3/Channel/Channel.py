#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, getopt
sys.path.insert(0, '/')
sys.path.insert(0, '../Constants')
sys.path.append('../Constants/')
from Constants.Constants import *
from ApiServer import MyApiServer
from ApiClient import MyApiClient
from threading import Thread

"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""
class Channel():
    """**************************************************
    Constructor de la clase
    @param <str> contact_ip: Si no se trabaja de manera local
    representa la ip del contacto con el que se
    establecera la conexion
    @param <int> my_port: De trabajar de manera local puerto
                de la instancia del cliente
    @param <int> contact_port: De trabajar de manera local
                representa el puerto de la instancia del contacto
    **************************************************"""
    def __init__(self, my_port, contact_port, interfaz, contact_ip = None):
        # Correrá en el fondo:
        self.interfaz = interfaz
        if contact_ip:
            con_local = False
        else:
            con_local = True
        servidor = MyApiServer(self.interfaz, con_local,  my_port = my_port)
        thread_servidor = Thread(target = servidor.serve)
        # Para que el thread se cierre al cerrar el programa:
        thread_servidor.daemon=True
        thread_servidor.start()
        self.client = MyApiClient(ip = contact_ip, my_port = contact_port)
        
    """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        self.client.muestra_texto(text)

    #Metodo para "colgar" (más bien suspender) la llamada.
    def colgar(self):
        self.client.colgar()

    #Método para regresar a la llamada o iniciar una nueva.
    def llamar(self):        
        self.llamadaThread = Thread(target=self.client.envia_audio)  
        self.llamadaThread.daemon = True        
        self.llamadaThread.start()

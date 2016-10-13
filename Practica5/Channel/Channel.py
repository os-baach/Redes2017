#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys, getopt
sys.path.insert(0, '/')
sys.path.insert(0, '../Constants')
sys.path.append('../Constants/')
import xmlrpclib
from Constants.Constants import *
from ApiServer import MyApiServer
from ApiClient import MyApiClient
from ApiServer import *
import threading
from threading import Thread

class ServidorUsers():

    def __init__(self, port, ip):
        self.port = port
        self.ip = ip
        self.server = xmlrpclib.Server('http://'+self.ip+':'+str(self.port))

    def registra(self,usr,ip,pto):
        self.server.registra(usr,ip,pto)

    def get_ip(self,usr):
        return self.server.get_ip(usr)

    def get_puerto(self,usr):
        return self.server.get_puerto(usr)

    def log_out(self,usr):
        return self.server.borra(usr)

    def get_nombres(self):
        return self.server.get_usuarios()

    def get_status(self,key):
        return self.server.get_status(key)

    def change_status(self, usr, yo,ip,puerto):
        self.server.change_status(usr,yo,ip,puerto)

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
    def __init__(self, my_port, contact_port, interfaz, contact_ip, usuario):
        self.users = ServidorUsers(contact_port,contact_ip)        
        # Correrá en el fondo:
        self.me = str(usuario)
        self.usr_temp = usuario
        self.interfaz = interfaz
        self.puerto = my_port
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
        lock = threading.Lock()
        with lock:
            self.users.registra(self.me,get_local_ip(),my_port)

    def set_temp_ajeno(self,usr,ip,port):
        self.usr_temp = usr
        new_ip = ip
        new_port = port
        self.client = MyApiClient(ip = new_ip, my_port = new_port)

    def set_temp(self,usr):
        self.usr_temp = usr
        new_ip = self.users.get_ip(usr)
        new_port = self.users.get_puerto(usr)
        self.client = MyApiClient(ip = new_ip, my_port = new_port)

    def log_out(self):
        self.users.log_out(self.me)

    def get_nombres(self):
        return self.users.get_nombres()

    def get_status(self,key):
        return self.users.get_status(key)
        
    def comienza_conver(self,usr):
        return self.users.change_status(usr,self.me,get_local_ip(),self.puerto)

    """**************************************************
    Metodo que se encarga de mandar texto al contacto con
    el cual se estableció la conexion
    **************************************************"""
    def send_text(self, text):
        self.client.muestra_texto(text)

    #Metodo para "colgar" (más bien suspender) la llamada.
    def colgar(self):
        self.client.colgar()
        
    #Metodo para iniciar la transmision de video.    
    def videollamar(self):
        self.videoThread = Thread(target=self.client.envia_video)
        self.videoThread.daemon = True
        self.videoThread.start()

    #Método para regresar a la llamada o iniciar una nueva.
    def llamar(self):        
        self.llamadaThread = Thread(target=self.client.envia_audio)  
        self.llamadaThread.daemon = True        
        self.llamadaThread.start()

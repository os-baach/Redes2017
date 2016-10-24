#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
import pyaudio
sys.path.append('../Constants/')
import SimpleXMLRPCServer
import xmlrpclib
from Constants.Constants import *
from numpy.lib import format as fmt
from cStringIO import StringIO
import threading
import cv2
import numpy as np
import numpy
import time
from PyQt4 import QtCore
from threading import Thread


#Función para optener nuestra ip local.
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip


class MyApiServerForever():

    def __init__(self,port,ip=None):
        self.port = port
        if ip is None:
            self.ip = get_local_ip()
        else:
            self.ip = ip
        self.usuarios = {}
        print(self.ip)
        self.server = SimpleXMLRPCServer.SimpleXMLRPCServer((self.ip, self.port), allow_none = True)
        self.server.register_instance(FunctionWrapperForever(self.usuarios))
        self.vivoThread = Thread(target=self.vivo)
        self.vivoThread.daemon = True
        self.vivoThread.start()


    def vivo(self):        
        while True:
            lock = threading.Lock()
            with lock:
                lock.acquire()
                if len(self.usuarios) > 0:
                    for key, value in self.usuarios.iteritems():
                        try:
                            ser = xmlrpclib.Server('http://' + value[0]  + ':' + str(value[1]))
                            ser.ping()
                        except:
                            del self.usuarios[key]
                lock.release()
            time.sleep(1)

    
    def serve(self):
        self.server.serve_forever()

class FunctionWrapperForever:

    def __init__(self,usuarios):
        self.usuarios = usuarios

    def registra(self,usuario,ip,puerto):
        self.usuarios[usuario] = [ip,puerto]

    def borra(self,usuario):
        del self.usuarios[usuario]

    def get_ip(self,usuario):
        return self.usuarios[usuario][0]

    def get_puerto(self,usuario):
        return self.usuarios[usuario][1]

    def get_usuarios(self):
        return self.usuarios

    def get_status(self,key):
        ip = self.usuarios[key][0]
        port = self.usuarios[key][1]
        try:            
            ser = xmlrpclib.Server('http://' + ip + ':' + str(port))
            return ser.get_status()
        except:
            return "Estado de error"

    def change_status(self,usr,desde,ip,puerto):
        ip = self.usuarios[usr][0]
        port = self.usuarios[usr][1]
        try:            
            ser = xmlrpclib.Server('http://' + ip + ':' + str(port))
            ser.change_status(desde,ip,puerto)
        except:
            print "El usuario no se encuentra disponible"

#Clase que representa mi propio servidor
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
        
# Definimos una clase para los metodos del servidor que queremos mandar y usar.        
class FunctionWrapper:
    def __init__(self,interfaz):
        self.interfaz = interfaz
        self.videocuadros = []
        self.videoT = None

    #Creamos el wrapper del sonido.
    def sendVoice_wrapper(self, audio):
        my_pyaudio = pyaudio.PyAudio()
        FORMAT = my_pyaudio.get_format_from_width(2)
        stream = my_pyaudio.open(format=FORMAT,
                        channels=1,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        data = audio.data
        stream.write(data)
        stream.close()
        my_pyaudio.terminate()
        
    # Funcion para detener el video    
    def stopImage_wrapper(self):
        cv2.destroyAllWindows()
        
    #Creamos el wrapper del video    
    def sendImage_wrapper(self, video):
        videoFinal = fmt.read_array(StringIO(video.data)) 
        self.videocuadros.append(videoFinal)
        if self.videoT == None:
	    p = threading.Thread(target=self.muestraImagen)
	    p.setDaemon(True)
            videoT = p
	    videoT.start()

    def ping(self):
        return "pong"

    def get_status(self):
        if self.interfaz.stackedWidget.currentIndex() == 1:
            return "Disponible"
        else:
            return "No disponible para iniciar conversación"

    def change_status(self,name,ip,puerto):
        if self.interfaz.stackedWidget.currentIndex() == 1:
            self.interfaz.stackedWidget.setCurrentIndex(2)
            self.interfaz.ventana_chat.clear()
            self.interfaz.ventana_chat.insertPlainText("El contacto: "+name+ " inicio un nuevo chat contigo! \n")
            self.interfaz.ventana_chat.insertPlainText("\n")
            self.interfaz.canal.set_temp_ajeno(name,ip,puerto)
        
    #Funcion auxiliar que usara el thread para mostrar los frames.
    def muestraImagen(self):
        while True:
            cv2.imshow('Video', self.videocuadros.pop(0))
                

    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        # Regresamos el mensaje pa' que lo agarre el servidor:
        self.interfaz.ventana_chat.insertPlainText("Contacto: "+message+ "\n")
        self.interfaz.ventana_chat.insertPlainText("\n")
        print message




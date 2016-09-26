#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
import pyaudio
sys.path.append('../Constants/')
import SimpleXMLRPCServer
from Constants.Constants import *
from Constants.Singleton import *
from numpy.lib import format as fmt
from cStringIO import StringIO
import threading
import cv2
import numpy as np
import numpy
from PyQt4 import QtCore

#Función para optener nuestra ip local.
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip

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
        self.interfaz.plainTextEdit.insertPlainText("Contacto: "+message+ "\n")
        self.interfaz.plainTextEdit.insertPlainText("\n")                
        print message




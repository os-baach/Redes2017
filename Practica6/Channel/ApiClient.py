#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../Constants/')
import xmlrpclib
from Constants.Constants import *
import multiprocessing
import threading
import pyaudio
import cv2
from numpy.lib import format as fmt
import numpy
from cStringIO import StringIO
"""Constantes para la reproduccion de audio. """

class MyApiClient:

    """ El ip y my_port son los ip y port de conexion. """
    def __init__(self, ip = None, my_port = DEFAULT_PORT):
        # El servidor que nos mandará el texto:
        self.llamada = False
        self.video = False
        self.my_port = my_port
        self.ip_dest = ip
        if not ip:
            self.server = xmlrpclib.Server('http://localhost:' + str(my_port))
        else:
            self.server = xmlrpclib.Server('http://' + ip  + ':' + str(my_port))

    """ Metodo que modifica nuestra variable de clase para saber cuando seguir transmitiendo. """        
    def colgar(self):
        self.llamada = False
        self.video = False

    def reiniciar(self):
        self.llamada = True
        self.video = True
        
    """Metodo para enviar video a nuestro servidor destino y agregarlo a una cola."""
    def envia_video(self):        
        self.queue_video = multiprocessing.Queue()
        self.hilo_video = threading.Thread(target=self.funcion_video, args=(self.server,))
        self.hilo_video.daemon = True
        self.hilo_video.start()        

    """ Metodo para enviar audio a nuestro servidor destino y agregarlo a una cola. """
    def envia_audio(self):
        if not self.llamada:
            self.reiniciar()
            self.queue = multiprocessing.Queue()
            self.hilo_llamada = threading.Thread(target=self.agrega_cola, args=(self.queue,))
            self.hilo_llamada.daemon = True
            self.hilo_llamada.start()
            if not self.ip_dest:
                self.server = xmlrpclib.ServerProxy('http://localhost:' +str(self.my_port), allow_none=True)
            else:
                self.server = xmlrpclib.Server('http://' + self.ip_dest  + ':' + str(self.my_port))            
            while self.llamada:
                datos_encolados = self.queue.get()
                data = xmlrpclib.Binary(datos_encolados)
                self.server.sendVoice_wrapper(data)
        
    """ En esta función se agrega a la cola el audio con data para transmitir al destino y encolar las grabaciones """    
    def agrega_cola(self, cola):
        self.pyaudio = pyaudio.PyAudio()
        self.pyaudio_format = self.pyaudio.get_format_from_width(2)
        self.stream = self.pyaudio.open(format=self.pyaudio_format, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        while self.llamada:
            frame = []
            for i in range(0,int(RATE/CHUNK *RECORD_SECONDS)):
                try:
                    frame.append(self.stream.read(CHUNK))
                except:
                    frame.append(self.stream.read(CHUNK))
            data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
            cola.put(data_ar)
    
    """ En esta funcion hacemos el envio del video al servidor """
    def funcion_video(self, cola):
        cap = cv2.VideoCapture(0)
	while self.video:
	    ret, frame = cap.read()
            f = StringIO()
	    fmt.write_array(f,frame)
	    data = xmlrpclib.Binary(f.getvalue())
	    cola.sendImage_wrapper(data)            	
        cap.release()
	cola.stopImage_wrapper()
        cv2.destroyAllWindows()


    # Muestra el texto recibido
    def muestra_texto(self, texto):
        # Espero esto sea lo que hay que hacer:
        self.server.sendMessage_wrapper(texto)

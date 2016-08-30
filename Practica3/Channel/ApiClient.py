#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../Constants/')
import xmlrpclib
from Constants.Constants import DEFAULT_PORT
import multiprocessing
import threading
import pyaudio
import numpy

CHUNK = 1024
RATE = 44100
RECORD_SECONDS = 2

class MyApiClient:

    def __init__(self, ip = None, my_port = DEFAULT_PORT):
        # El servidor que nos mandará el texto:
        self.llamada = False
        self.my_port = my_port
        self.ip_dest = ip
        if not ip:
            self.server = xmlrpclib.Server('http://localhost:' + str(my_port))
        else:
            self.server = xmlrpclib.Server('http://' + ip  + ':' + str(my_port))
            
    def colgar(self):
        self.llamada = False
            
            
    def envia_audio(self):
        if not self.llamada:
            self.llamada = True
            self.queue = multiprocessing.Queue()
            self.hilo_llamada = threading.Thread(target=self.agrega_cola, args=(self.queue,))
            self.hilo_llamada.daemon = True
            self.hilo_llamada.start()
            if not self.ip_dest:
                self.proxy = xmlrpclib.ServerProxy('http://localhost:' +str(self.my_port), allow_none=True)
            else:
                self.server = xmlrpclib.Server('http://' + self.ip_dest  + ':' + str(self.my_port))            
            while self.llamada:
                datos_encolados = self.queue.get()
                data = xmlrpclib.Binary(datos_encolados)
                self.proxy.sendVoice_wrapper(data)            
            
    def agrega_cola(self, cola):
        self.pyaudio = pyaudio.PyAudio()
        self.pyaudio_format = self.pyaudio.get_format_from_width(2)
        self.stream = self.pyaudio.open(format=self.pyaudio_format, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        while True:
            frame = []
            for i in range(0,int(RATE/CHUNK *RECORD_SECONDS)):
                frame.append(self.stream.read(CHUNK))
            data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
            cola.put(data_ar)

    # Muestra el texto recibido
    def muestra_texto(self, texto):
        # Espero esto sea lo que hay que hacer:
        self.server.sendMessage_wrapper(texto)

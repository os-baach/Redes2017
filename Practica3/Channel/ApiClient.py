#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../Constants/')
import xmlrpclib
import pyaudio
import wave
import array
from Constants.Constants import *

class MyApiClient:

    def __init__(self, ip = None, my_port = DEFAULT_PORT):
        # El servidor que nos mandará el texto:
        if not ip:
            self.server = xmlrpclib.Server('http://localhost:' + str(my_port))
        else:
            self.server = xmlrpclib.Server('http://' + ip  + ':' + str(my_port))

    # Muestra el texto recibido
    def muestra_texto(self, texto):
        # Espero esto sea lo que hay que hacer:
        self.server.sendMessage_wrapper(texto)

    # Graba el audio
    def graba(self):
        cadena_total = ''
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        print("*recording")
        frames = []
        for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
            data  = stream.read(CHUNK)
            cadena_total += array.array('B', data).tostring()
            frames.append(data)
        print("*done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()
        print("*closed")
        return self.server.echo_audio_wrapper(cadena_total)

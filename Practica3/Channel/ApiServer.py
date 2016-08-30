#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
import pyaudio
import wave
import time
sys.path.append('../Constants/')
import SimpleXMLRPCServer
from Constants.Constants import *
from Constants.Singleton import *


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    ip = s.getsockname()[0]
    s.close()
    return ip

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

    # Creo que ésto ya lee audio :v
    def echo_audio_wrapper(self, data):
        frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(WIDTH),
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)
        for datos in data:
            stream.write(data)
            frames.append(data)                    
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        stream.stop_stream()
        stream.close()
        p.terminate()

        
        
class FunctionWrapper:
    def __init__(self,interfaz):
        self.interfaz = interfaz

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

    

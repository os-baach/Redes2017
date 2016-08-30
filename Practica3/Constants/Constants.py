#! /usr/bin/env python
import pyaudio
from Singleton import *

MENSAJE_VISTA = OnlyOne(None)
DEFAULT_PORT = 5000
CHUNK = 1024 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "server_output.wav"
WIDTH = 2

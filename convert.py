#!/usr/bin/env python3

import speech_recognition as sr
# from pathlib import path
import sys

input_file = sys.argv[1]

r = sr.Recognizer()
with sr.AudioFile(input_file) as source:
    audio = r.record(source)

# recognize speech using Sphinx
try:
    text = r.recognize_sphinx(audio)
except sr.UnknownValueError:
    print("Error: sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

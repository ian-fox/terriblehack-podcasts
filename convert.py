#!/usr/bin/env python3

import speech_recognition as sr
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

r = sr.Recognizer()
with sr.AudioFile(input_file) as source:
    audio = r.record(source)

text = ""

# recognize speech using Sphinx
try:
    text = r.recognize_sphinx(audio)
except sr.UnknownValueError:
    print("Error: sphinx could not understand audio")
    sys.exit(1)
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
    sys.exit(1)

# Print transcript
print(text)

# Speak text with google text to speech
from gtts import gTTS
tts = gTTS(text)
tts.save(output_file)

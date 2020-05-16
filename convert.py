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
# try:
#     text = r.recognize_sphinx(audio)
# except sr.UnknownValueError:
#     print("Error: sphinx could not understand audio")
#     sys.exit(1)
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))
#     sys.exit(1)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    text = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Error: Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Error: Could not request results from Google Speech Recognition service; {0}".format(e))

# Print transcript
print(text)

# Speak text with google text to speech
from gtts import gTTS
tts = gTTS(text)
tts.save(output_file)

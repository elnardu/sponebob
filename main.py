#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import random
from PIL import Image, ImageDraw, ImageFont

def generateImage(text):
    im = Image.open('./meme.jpg')
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype('./impact.ttf', 40)
    w, h = im.size
    w1, h1 = d.multiline_textsize(text, font=font)
    d.multiline_text((w/2 - w1/2, 10), text, font=font, fill='white', align='center')
    im.save('./newmeme.jpg')


# generateImage('Lorem ipsum dolor sit amet\nqwjrgqwgekqugwekqgwkeu')

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)


# recognize speech using Wit.ai
WIT_AI_KEY = "C6BJSC3PLMPUFCTRK3ZXC4GOD533MDKI"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    s = ""
    i = 0 
    for c in r.recognize_wit(audio, key=WIT_AI_KEY):
        if random.randint(0, 1):
            s += c.upper()
        else:
            s += c
        i+=1
        if i == 15:
            i = 0
            s+='\n'
    print(s)
    generateImage(s)




except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))



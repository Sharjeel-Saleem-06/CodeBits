import os
import pyttsx3
import speech_recognition as sr  
import tkinter.messagebox as tmessage
from os.path import exists
import wolframalpha


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
wolfprime_app='AWXVV8-7Q3HUJ43K5'


def audio(message):
    engine.say(message)
    engine.runAndWait()


def welcome():
    print("Welcome to Calculator")
    audio('welcome to calculator')
    print('If you want to calculate something, please say "calculate" followed by your expression')
    audio('If you want to calculate something, please say "calculate" followed by your expression')
    print('For example, "calculate 7 plus 8" or "calculate sin 30 plus cot 20"')
    audio('For example, "calculate 7 plus 8" or "calculate sin 30 plus cot 20"')   


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio('Listening...')
        r.pause_threshold=2
        r.energy_threshold=3000
        audio_data=r.listen(source)
import os
import pyttsx3
import speech_recognition as sr  
import tkinter.messagebox as tmessage
from os.path import exists
import wolframalpha


listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')



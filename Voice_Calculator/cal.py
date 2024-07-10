import os
import pyttsx3
import speech_recognition as sr  
import tkinter.messagebox as tmessage
from os.path import exists
import wolframalpha

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
wolfprime_app = 'AWXVV8-7Q3HUJ43K5'
is_paused = False

def audio(message):
    engine.say(message)
    engine.runAndWait()

def welcome():
    print("Welcome to Calculator")
    audio('Welcome to Calculator')
    print('If you want to calculate something, please say "calculate" followed by your expression')
    audio('If you want to calculate something, please say "calculate" followed by your expression')
    print('For example, "calculate 1 plus 2" or "calculate cos 10 plus cot 10"')
    audio('For example, "calculate 1 plus 2" or "calculate cos 10 plus cot 10"')   

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio('Listening...')
        listener.pause_threshold = 2
        listener.energy_threshold = 3000
        audio_data = listener.listen(source)
    try:
        print("Recognizing")
        audio("Recognizing")
        query = listener.recognize_google(audio_data, language='en-In')
        print(query)
    except Exception as e:
        tmessage.showinfo('Error', f'{e}')
        print("Can you please repeat?")
        return "NONE"
    return query.lower()

def calculate():
    client = wolframalpha.Client(wolfprime_app)
    indx = spech.split().index('calculate')
    query = spech.split()[indx + 1:]
    res = client.query(' '.join(query))
    try:
        answer = next(res.results).text
    except StopIteration:
        tmessage.showinfo('Error', 'No results found')
        return

    final_answer = f"Your Query was: {' '.join(query)}\nYour answer is: {answer}\n"
    os.makedirs('Voice Calculator', exist_ok=True)

    with open(r'maths.txt', 'a', encoding='utf-8') as file:
        file.write(final_answer)

    print("The answer is " + answer)
    audio("The answer is " + answer)

welcome()

while True:
    if not is_paused:
        spech = take_command()

        if 'calculate' in spech:
            calculate()
        elif 'clear' in spech:
            if exists(r'maths.txt'):
                with open(r'maths.txt', 'r+') as file:
                    file.truncate(0)
                print('History cleared')
                audio('History cleared')
            else:
                tmessage.showinfo("Error", "No file exists")
        elif 'pause' in spech:
            is_paused = True
            print("Paused")
            audio("Paused")
        elif 'quit' in spech or 'exit' in spech:
            quit()
        else:
            tmessage.showinfo('Oops', "Didn't understand")
    else:
        spech = take_command()

        if 'resume' in spech:
            is_paused = False
            print("Resumed")
            audio("Resumed")
        else:
            print("Paused. Say 'resume' to continue.")
            audio("Paused. Say 'resume' to continue.")

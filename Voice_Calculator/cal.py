import os  # Provides functions for interacting with the operating system
import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Library for performing speech recognition
import tkinter.messagebox as tmessage  # Module for showing message boxes in Tkinter GUI
from os.path import exists  # Function to check if a path exists
import wolframalpha  # WolframAlpha API client library

# Initialize the speech recognizer and text-to-speech engine
listener    =    sr.Recognizer()
engine      =    pyttsx3.init()

# Set the voice for the text-to-speech engine
voices  =    engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# WolframAlpha API key
wolfprime_app   =    'AWXVV8-7Q3HUJ43K5'

# Variable to track if the application is paused
is_paused = False

# Function to convert text to speech and play it
def audio(message):
    engine.say(message)
    engine.runAndWait()

# Function to welcome the user and provide initial instructions
def welcome():
    print("Welcome to Calculator")
    audio('Welcome to Calculator')
    print('If you want to calculate something, please say "calculate" followed by your expression')
    audio('If you want to calculate something, please say "calculate" followed by your expression')
    print('For example, "calculate 1 plus 2" or "calculate cos 10 plus cot 10"')
    audio('For example, "calculate 1 plus 2" or "calculate cos 10 plus cot 10"')

# Function to take a voice command from the user
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio('Listening...')
        listener.pause_threshold = 2  # Adjusts the pause threshold for speech recognition
        listener.energy_threshold = 3000  # Adjusts the energy threshold for ambient noise
        audio_data = listener.listen(source)  # Listens for the user's input
    try:
        print("Recognizing")
        audio("Recognizing")
        query = listener.recognize_google(audio_data, language='en-In')  # Recognizes the speech using Google API
        print(query)
    except Exception as e:
        tmessage.showinfo('Error', f'{e}')  # Shows error message if recognition fails
        print("Can you please repeat?")
        return "NONE"
    return query.lower()

# Function to perform the calculation using WolframAlpha
def calculate():
    client = wolframalpha.Client(wolfprime_app)  # Initialize the WolframAlpha client
    indx = spech.split().index('calculate')  # Find the index of 'calculate' in the command
    query = spech.split()[indx + 1:]  # Extract the calculation query from the command
    res = client.query(' '.join(query))  # Send the query to WolframAlpha
    try:
        answer = next(res.results).text  # Get the result from WolframAlpha
    except StopIteration:
        tmessage.showinfo('Error', 'No results found')  # Show error message if no results found
        return

    final_answer = f"Your Query was: {' '.join(query)}\nYour answer is: {answer}\n"
    os.makedirs('Voice Calculator', exist_ok=True)  # Create directory if it doesn't exist

    with open(r'maths.txt', 'a', encoding='utf-8') as file:
        file.write(final_answer)  # Save the result to a file

    print("The answer is " + answer)
    audio("The answer is " + answer)  # Speak out the answer

# Welcome the user
welcome()

# Main loop to continuously take commands and perform actions
while True:
    if not is_paused:
        spech = take_command()  # Get the command from the user

        if 'calculate' in spech:
            calculate()  # Perform calculation if 'calculate' is in the command
        elif 'clear' in spech:
            if exists(r'maths.txt'):
                with open(r'maths.txt', 'r+') as file:
                    file.truncate(0)  # Clear the history if the file exists
                print('History cleared')
                audio('History cleared')
            else:
                tmessage.showinfo("Error", "No file exists")  # Show error if file doesn't exist
        elif 'pause' in spech:
            is_paused = True  # Pause the application
            print("Paused")
            audio("Paused")
        elif 'quit' in spech or 'exit' in spech:
            quit()  # Exit the application
        else:
            tmessage.showinfo('Oops', "Didn't understand")  # Show error if command is not recognized
    else:
        spech = take_command()  # Get the command if paused

        if 'resume' in spech:
            is_paused = False  # Resume the application
            print("Resumed")
            audio("Resumed")
        else:
            print("Paused. Say 'resume' to continue.")  # Prompt user to resume if paused
            audio("Paused. Say 'resume' to continue.")

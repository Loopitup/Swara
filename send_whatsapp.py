import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
updates = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def send_whatsapp():
    what_num = int(input("Enter the phone number of the person you want message:-\n"))
    message = takeCommand()
    pywhatkit.sendwhatmsg(f"+91{what_num}", message, time_hour=strTime, time_min=updates)
    speak("Message has been send")

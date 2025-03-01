from time import sleep
from googletrans import Translator
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound
import time
from maingui import GuiofFoxxy

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

def translate_(query):
    speak("Sure Sir")
    print(googletrans.LANGUAGES)
    translator = Translator(service_urls=['translate.googleapis.com'])
    speak("Choose the language in which you wnat to translate")
    b = input("enter the language:- ")
    text_to_translate = translator.translate(query,src="auto",dest=b)
    trans_text = text_to_translate.text
    try:
        ui.terminalprint(f"{trans_text}")
        speakgl = gTTS(text=trans_text, lang=b, slow= False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")

        time.sleep(5)
        os.close("voice.mp3")
    except:
        print("\n")

ui = GuiofFoxxy()

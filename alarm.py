import pyttsx3
import datetime
import os 
import speech_recognition as sr
from pygame import mixer

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("swara","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ", ":")

    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            mixer.init()
            mixer.music.load("alarm_ringtone.mp3")
            mixer.music.play()
            query = takeCommand().lower()
            if 'turn off alarm' in query or 'turn of alarm' in query:
                mixer.music.pause()
                speak("alarm has been turned off")
        elif currenttime + "00:00" == Alarmtime:
            exit()

ring(time)

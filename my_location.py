import pyttsx3
import speech_recognition as sr
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def myLocation():
    speak("wait sir, let me check")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        url = f'https://api.ipify.org/{ipAdd}'
        geo_requests = requests.get(url)
        geo_data = json.load(geo_requests)
        city = geo_data['city']
        print(geo_data)
        state = geo_data['state']
        country = geo_data['country']
        print(f"I am not sure, but i think we are in {city} state of {country}")
        speak(f"I am not sure, but i think we are in {city} state of {country}")
    except Exception as e:
        speak("Sorry sir, Due to network issue i am not able to find where we are.")
        pass

myLocation()

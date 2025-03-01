import pyttsx3
import datetime
import requests
import os
import pygame


def speak(data):
    voice = 'hi-IN-SwaraNeural'
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    



def wishMe():
    #wishes you
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Jai jinendra. Good Morning!. I am Swara sir. Please tell me how may i help you?")

    elif hour>=12 and hour<18:
        speak("Jai jinendra. Good Afternoon!. I am Swara sir. Please tell me how may i help you?")

    else:
        speak("Jai jinendra. Good Evening!. I am Swara sir. Please tell me how may i help you?") 

def bye_by():
    #Swara shuts down and say good bye to you
    hr = int(datetime.datetime.now().hour)
    if hr>=5 and hr<12:
        response = requests.get("https://zenquotes.io/api/quotes/keywords=inspiration")
        if response.status_code == 200:    
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']

            print(f"{quote} - {author}")
            speak(f"{quote} - {author}")
        speak("Good Morning Sir!, have a nice day. See you soon!")

    elif hr>=12 and hr<17:
        speak("Good Afternoon Sir!. I hope you are having a good day. See you soon!") 

    elif hr>=17 and hr<21:
        speak("Good Evening Sir!. I hope you enjoyed your day. See you soon!")

    else:
        response = requests.get("https://zenquotes.io/api/quotes/keywords=hapiness")
        if response.status_code == 200:    
            data = response.json()
            quote = data[0]['q']
            author = data[0]['a']

            print(f"{quote} - {author}")
            speak(f"{quote} - {author}")
        speak("Put your worries aside and have a baby like sleep tonight. Good Night Sir!. See you soon!")

bye_by()


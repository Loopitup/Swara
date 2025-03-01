import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import sys
import os
from os import environ
environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import smtplib
import pyjokes
import requests
import pyautogui
import speedtest
import pywhatkit
import time
import subprocess
import random
from time import sleep
from plyer import notification
from pygame import mixer
from bs4 import BeautifulSoup




for i in range(3): 
    a = input("Enter Password To Continue: ")
    pw = "TNT1234"
    if (a==pw):
        print("WELCOME SIR! PLEASE SPEAK [WAKE UP] TO LOAD ME UP")
        break
    else:
        print("Try again")

from intro import play_gif
play_gif

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

def  alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


    
if __name__ == "__main__":

    while True:
        query = takeCommand().lower()

        # Logic for execution of task based on query
        if 'wake up' in query:
            from Wishme import wishMe
            wishMe()

            while True:
                query = takeCommand().lower()
                if 'go to sleep' in query:
                    speak("Ok Sir!, you can call me anytime")
                    break
                elif 'exit' in query or 'bye' in query:
                    from Wishme import bye_by
                    bye_by()
                    exit()

                elif 'hello' in query:
                    speak("Hello Sir!, how are you?")
                
                elif 'how is the josh' in query:
                    speak("High Sir!!!!!!")
                
                elif 'i am fine' in query or 'i am good' in query:
                    speak("Good to hear that, Sir!")

                elif 'how r u' in query or 'how are you' in query:
                    speak("perfect sir")
                
                elif 'thank' in query:
                    speak("you are welcome sir!")
                
                elif 'good work' in query or "good job" in query:
                    speak("It's my pleasure helping you sir!. Anything else i can do sir!")

                elif 'good night' in query:
                        speak("Good night Sir")
                    
                elif 'good morning' in query:
                        speak("good morning Sir")
                    
                elif 'good evening' in query:
                        speak("good evening Sir")

                elif 'good afternoon' in query:
                        speak("good afternoon Sir")
                
                elif 'tell me about yourself' in query:
                    print("Hi my name is Swara, i am your desktop assistant/AI friend programmed by Sambhav Jain sir in such a way that i will make your life more scheduled and easy. For more information please seek help....")
                    speak("Hi my name is Swara, i am your desktop assistant/AI friend programmed by Sambhav Jain sir in such a way that i will make your life more scheduled and easy. For More information please seek help....")
                
                elif "what's up" in query or 'what is up' in query or 'what you doing' in query:
                        choose = ("just vibing on tauba tauba", "just here to help you")
                        choosed = random.choice(choose)
                        speak(choosed)
                    
                elif 'what are your hobbies' in query:
                    speak("As i am a virtual assistant, i don't have such hobbies but i like to learn as much as i can and i like to do complex mathematic calculations and want to explore the world of humans")
                
                elif 'help' in query or 'what are you capable of' in query or 'what can you do' in query:
                        with open("helps.txt",'r') as file:
                            about_me = file.read()
                            print(about_me)
                            file.close()

                elif "what's your name" in query or 'what is your name' in query:
                    speak("Hi, my name is Swara")

                elif 'google' in query:
                    from Search_now import searchgoogle
                    searchgoogle(query)

                elif 'youtube' in query:
                    from Search_now import searchyoutube
                    searchyoutube(query)
                
                elif 'wikipedia' in query:
                    from Search_now import searchwikipedia
                    searchwikipedia(query)
                    
                elif 'where i am' in query or 'where we are' in query:
                    from my_location import myLocation
                    myLocation()

                elif 'calculate' in query:
                    from calculate import WolframaAlpha
                    from calculate import calc
                    query = query.replace("calculate","")
                    query = query.replace("foxy","")
                    calc(query)

                elif 'battery' in query:
                   from battery_l import battary_level
                   battary_level()

                elif 'news' in query:
                    from NewsRead import latestnews
                    latestnews()

                elif 'read a pdf' in query:
                    from pdf_reader import read_pdf
                    read_pdf()

                elif 'set an alarm' in query:
                    print("Tell me the time like example:- 10:10:10")
                    a = input("enter the time :- ")
                    alarm(a)
                    speak("Alarm has been set")

                elif 'whatsapp' in query:
                    from send_whatsapp import send_whatsapp
                    send_whatsapp()

                elif 'where is' in query:
                    from geopy.geocoders import Nominatim
                    loc = Nominatim(user_agent="GetLoc")
                    query = query.replace("where is","")
                    query = query.replace("foxy","")
                    getloc = loc.geocode(f"{query}")
                    print(getloc.address)

                elif 'direction' in query:
                    query = query.replace("tell me the direction of","")
                    query = query.replace("foxy","")
                    query = query.replace("direaction","")
                    
                    search = query
                    url = f"https://www.google.co.in/maps/place/{search}"
                    webbrowser.open(url)

                elif 'date' in query:
                    from datetime import date
                    today_date = date.today()
                    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                    today_day = days[today_date.weekday()]
                    print(f"Sir today's date is {today_date} and the day is {today_day}")
                    speak(f"Sir today's date is {today_date} and the day is {today_day}")

                elif 'time' in query:
                    strtime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Sir the time is {strtime}")
                    speak(f"Sir the time is {strtime}")

                elif 'open' in query:
                    from Dictapp import openappweb
                    openappweb(query)
                    
                elif 'close' in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif 'pause' in query:
                    pyautogui.press("space")
                    speak("video paused")
                elif 'resume' in query:
                    pyautogui.press("space")
                    speak("video played")
                elif 'mute' in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif 'increase volume' in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif 'decrease volume' in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()
                elif 'switch tab' in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    pyautogui.press("enter")
                    time.sleep(2)

                elif 'music' in query:
                    speak("Which song you want me to play?")
                    song_name = takeCommand().lower()
                    pywhatkit.playonyt(song_name)

                elif 'play a game' in query:
                    print("Which game do you wanna play stone paper scissor or odd even:")
                    game_name = input()
                    if 'stone paper scissor' == game_name:
                        from rock_paper_scissor import play_rps
                        play_rps()
                    elif 'odd even' == game_name:
                        from odd_even import oddeven
                        oddeven() 

                elif 'temperature' in query:
                    search = query
                    url = f"https://www.google.co.in/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    print(f"current temperature in that place is {temp}")
                    speak(f"current temperature in that place is {temp}")

                elif 'weather' in query:
                    search = query
                    url = f"https://www.google.co.in/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    weather = data.find("div", class_ = "BNeawe tAd8D AP7Wnd").text
                    climate_info = weather.split('\n')
                    time = climate_info[0]
                    sky = climate_info[1]
                    print(f"current weather in that place is {sky}")
                    speak(f"current weather in that place is {sky}")

                elif 'internet speed' in query:
                    speak("Wait, Calculating your internet speed")
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576     # 1Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048579
                    print("Wifi download speed is",download_net,"MBps")
                    print("Wifi upload speed is",upload_net,"MBps")
                    speak(f"Wifi download speed is,{download_net},MB p s")
                    speak(f"Wifi upload speed is,{upload_net},MB p s")

                elif 'remember that' in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("foxy","")
                    speak("You told me to"+rememberMessage)
                    remember = open("Remember.txt","w")
                    remember.write(rememberMessage)
                    remember.close()

                elif 'what did i told you to remember' in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read())

                elif 'joke' in query:
                    joke_1 = pyjokes.get_joke(language='en', category='all')
                    print(joke_1)
                    speak(joke_1)

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz type YES or NO)")
                    a = input("yes/no:- ")
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif 'show my schedule' in query:
                     file = open("tasks.txt","r")
                     content = file.read()
                     file.close()
                     mixer.init()
                     mixer.music.load("notification.mp3")
                     mixer.music.play()
                     notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 30
                        )
                     
                elif "focus mode" in query:
                    a = (input("Are you sure that you want to enter focus mode (yes/no):- "))
                    b = (input("Do you want to restart your focus progress: "))
                    if (a=="yes"):
                        if (b=="yes"):
                            file = open("Focus.txt","w")
                            file.write("0")
                            file.close()
                            speak("Your focus progress has been reset")
                            speak("Entering the focus mode....")
                            os.startfile("focusmode.py")
                        elif (b=="no"):
                            speak("Entering the focus mode....")
                            os.startfile("focusmode.py")
                    else:
                        pass

                elif "focus progress" in query:
                    from focus_graph import focusgraph
                    focusgraph()

                elif 'screenshot' in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif 'click my photo' in query:
                    subprocess.run("start microsoft.windows.camera:", shell=True)
                    speak("Say cheese")
                    pyautogui.press("enter")
                    subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)

                elif 'translate' in query:
                    from Translator import translate_
                    query = query.replace("foxy","")
                    query = query.replace("translate","")
                    translate_(query)

                elif 'shutdown' in query:
                    speak("Are you sure you want to shutdown your system?")
                    shutdown = input("Do you wish to shutdown your system? (yes/no)\n")
                    if shutdown == "yes":
                     os.system("shutdown /s /t 5")

                    elif shutdown == "no":
                        break
                
                elif 'restart the system' in query:
                    speak("Restarting your system")
                    os.system("shutdown /r /t s")
                
                elif 'sleep the system' in query:
                    speak("Turning on the sleep mode")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        






            


import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dict_app = {"vscode":"code", "notepad":"notepad", "wordpad":"wordpad", "paint":"mspaint",
             "cmd":"cmd", "microsoft edge":"msedge", "pycharm":"pycharm64", "vlc":"vlc", "chrome":"chrome",
             "ms word":"Winword", "ms excel":"excel", "power point":"powerpnt", "outlook":"outlook", "unity":"unity",
             "adobe acrobat":"acrobat", "brave":"brave", "spotify":"spotify", "zoom":"zoom", "teams":"teams"}

def openappweb(query):
    speak("Launching, sir!")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("foxy","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    
    else:
        keys = list(dict_app.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dict_app[app]}")

def closeappweb(query):
    speak("closing, sir!")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5) 
        speak("All tabs closed")
    elif "3 tab" in query or "three tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "4 tab" in query or "four tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")
    elif "5 tab" in query or "five tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("All tabs closed")

    keys = list(dict_app.keys())
    for app in keys:
         if app in query:
            os.system(f"Taskkill /f /im {dict_app[app]}.exe")
        

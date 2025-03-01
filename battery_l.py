import psutil
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def battary_level():
    data = psutil.sensors_battery()
    percentage =  data.percent
    charge_stat = data.power_plugged
    battery_ = percentage
    if(charge_stat==True):
        speak(f"Sir your system have {percentage} percentage battery and is currently being charged")
    else:
        speak(f"Sir your system have {percentage} percentage battary")
        if battery_>=75:
            speak("Your system have enough power to continue your work")
        elif battery_>40 and battery_<75:
            speak("You can charge your system if you wish")
        elif battery_>15 and battery_<=40:
            speak("Battery level is low. PLease charge your system")
        elif battery_<=15:
            speak("Battery level is very low. Your system is running on low power mode. PLease charge your system")
    
battary_level()

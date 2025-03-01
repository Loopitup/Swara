import pyttsx3
import speech_recognition as sr
import random

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
        query = r.recognize_google(audio, language='enin')
        print("User said:", query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def oddeven():
    speak("Let's play odd even!")
    print("let's start!")
    my_score = 0
    Swara_score = 0
    i = 0

    while(i<3):
        query = takeCommand().lower()
        choose = ("1","2","3","4","5","6")
        Swara_num = random.choice(choose)

        if (query == "i choose even number"):
            speak("I choose odd")
            my_num = takeCommand().lower()
            my_num = my_num.replace("one","1")
            my_num = my_num.replace("two","2")
            my_num = my_num.replace("three","3")
            my_num = my_num.replace("four","4")
            my_num = my_num.replace("five","5")
            my_num = my_num.replace("six","6")
            speak(Swara_num)
            sum = my_num+Swara_num
            if (sum%2)==0:
                speak("You won")
            else:
                speak("I won")

        elif (query == "i choose odd number"):
            speak("I choose even")
            my_num = takeCommand().lower()
            my_num = my_num.replace("one","1")
            my_num = my_num.replace("two","2")
            my_num = my_num.replace("three","3")
            my_num = my_num.replace("four","4")
            my_num = my_num.replace("five","5")
            my_num = my_num.replace("six","6")
            speak(Swara_num)
            sum = my_num+Swara_num
            if (sum%2) == 0:
                speak("I won")
            else:
                speak("You won")           
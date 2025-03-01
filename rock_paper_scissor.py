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

def play_rps():
    speak("Let's play stone paper scissor!")
    print("Let's start!")
    i = 0
    my_score = 0
    Swara_score = 0

    while(i<5):
        choose = ("rock","paper","scissor")
        Swara_choice = random.choice(choose)
        query = takeCommand().lower()

        if (query == "stone"):
            if (Swara_choice == "stone"):
                speak("STONE")
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
            elif (Swara_choice == "paper"):
                speak("PAPER")
                Swara_score +=1
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
            else:
                speak("SCISSOR")
                my_score +=1
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")

        elif (query == "paper"):
            if (Swara_choice == "stone"):
                speak("STONE")
                my_score +=1
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
            elif (Swara_choice == "paper"):
                speak("PAPER")
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
            else:
                speak("scissor")
                Swara_score +=1
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")

        elif (query == "scissor"):
            if (Swara_choice == "stone"):
                speak("STONE")
                Swara_score +=1
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
            elif (Swara_choice == "paper"):
                speak("PAPER")
                my_score +=1
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
            else:
                speak("SCISSOR")
                print(f"SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
        i +=1

    print(f"FINAL SCORE:\nMY : {my_score}\nSwara : {Swara_score}")
    speak("Game has ended")
    if (my_score>Swara_score):
        speak("You won")
    elif (Swara_score<my_score):
        speak("I won")
    else:
        speak("It's a draw")

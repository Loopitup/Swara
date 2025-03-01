import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    apidict = {"business":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=apikey",
                "science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=apikey",
                "sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=apikey",
                "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=apikey",
                "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=apikey",
                "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=apikey"}
    
    content = None
    url = None
    print("Which field news do you want, [business], [science], [sports], [technology], [entertainment], [health]")
    speak("Which field news do you want, [business], [science], [sports], [technology], [entertainment], [
    field = input("Enter the field:- ")
    for key, value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("urll not found")
            break
        else:
            url = True
            if url is True:
                print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print("for more info visit: {news_url}")

        a = input("[press 1 to continue] and [press 2 to stop]\n")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("that's all")

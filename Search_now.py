import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():

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

query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchgoogle(query):
    if 'google' in query:
        import wikipedia as googleScrap
        query = query.replace("swara","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def searchyoutube(query):
    if 'youtube' in query:
        speak("This is what i found for your search!")
        query = query.replace("swara","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        speak("Shall i play it")
        play_ = takeCommand().lower()
        if 'yes' in query:
            pywhatkit.playonyt(query)
        elif 'no' in query:
            speak("Ok sir")
        speak("Done, sir!")

def searchwikipedia(query):
    if 'wikipedia' in query:
        speak("Searching from wikipedia...")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("swara","")
        results = wikipedia.summary(query,sentences =1)
        speak("According to wikipedia...")
        print(results)
        speak(results)

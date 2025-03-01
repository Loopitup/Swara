import wolframalpha
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WolframaAlpha(query):
    apikey = "api_key"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def calc(query):
    Term = str(query)
    Term = Term.replace("foxy","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("divide","/")
    Term = Term.replace("minus","*")
    
    final = str(Term)
    try:
        result = WolframaAlpha(final)
        print(f"{result}")
        speak(result)
    except:
        speak("The value is not answerable")


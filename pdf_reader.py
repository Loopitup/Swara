from pypdf import PdfReader
import pyttsx3
import speech_recognition as sr

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
def read_pdf():
    print("Go to your file location then select your pdf\nhold shift and right click on it then left click on copy as path ")
    a = input("Enter/paste your file path:- ")
    reader = PdfReader(f"{a}")
    nop_ = len(reader.pages)
    speak(f"This pdf has {nop_} number of pages")
    speak("Please tell me page you want me to read")
    pg = int(input("Enter the pages number:- "))
    page = reader.pages[pg]
    text = page.extract_text()
    print(text)
    speak(text)

read_pdf()

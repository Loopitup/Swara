import time
import datetime
import ctypes
import sys
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin:
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter the time eg:- 10:10 :-\n")
    a = current_time.replace(":",".")
    a = float(a)
    b = stop_time.replace(":",".")
    b = float(b)
    Focus_time = b-a
    Focus_time = round(Focus_time,3)                  
    host_path = "C:\Windows\System32\drivers\etc\hosts"
    redirected = "127.0.0.1 "

    print(current_time)
    time.sleep(2)
    website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com", "www.youtube.com",
                     "youtube.com", "www.twitter.com", "twitter.com", "www.amazon.in", "amazon.in", "flipkart.com",
                     "www.flipkart.com", "open.spotify.com", "spotify.com", "www.spotify.com", "www.netflix.com",
                     "netflix.com", "www.crunchyroll.com", "crunchyroll.com"]
    if(current_time < stop_time):
        with open(host_path,"r+") as file:
            content = file.read()
            time.sleep(2)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirected} {website}\n")

                    time.sleep(1)
            print("FOCUS MODE HAS BEEN TURNED ON")
            speak("Focus mode has been turned on")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com", "www.youtube.com",
                     "youtube.com", "www.twitter.com", "twitter.com", "www.amazon.in", "amazon.in", "flipkart.com",
                     "www.flipkart.com", "open.spotify.com", "spotify.com", "www.spotify.com", "www.netflix.com",
                     "netflix.com", "www.crunchyroll.com", "crunchyroll.com"]
        if(current_time >= stop_time):
            with open(host_path,"r+") as file:
                content = file.readlines()
                file.seek(0)

                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)

                file.truncate()

                speak("FOCUS MODE HAS ENDED")
                file = open("Focus.txt","a")
                file.write(f",{Focus_time}")
                file.close()
                break
        
else:
    ctypes.windll.shell32.ShellEexcution(None,"runas",sys.executable," ".join(sys.argv),None, 1)

is_admin()
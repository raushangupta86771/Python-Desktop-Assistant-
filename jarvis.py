import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning Sir !!")
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon sir")
    else:
        print("Good Evening sir")

    speak("I am Jarvis. sir, please tell how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        speak("Say that again please...")
        return "None"  # None string will be returned
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    f = open('name.txt', 'r')
    data = f.read()
    f.close()
    server.login('raushangupta2231@gmail.com', data)
    server.sendmail('raushangupta2231@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            speak("Opening google ")
            webbrowser.open("google.com")
        elif 'open vtop' in query:
            speak("Opening V top ")
            webbrowser.open("vtop.vit.ac.in")
        elif 'open twitter' in query:
            speak("Opening twitter ")
            webbrowser.open("twitter.com")
        elif 'open gmail' in query:
            speak("Opening gmail ")
            webbrowser.open("gmail.com")
        elif 'open facebook' in query:
            speak("Opening facebook ")
            webbrowser.open("facebook.com")
        elif 'open insta' in query:
            speak("Opening insta ")
            webbrowser.open("instagram.com")
        elif 'open youtube' in query:
            speak("Opening Youtube ")
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'D:\song'
            songs = os.listdir(music_dir)
            rand = random.randint(1, 5)
            os.startfile(os.path.join(music_dir, songs[rand]))
            quit(0)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\raush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Successfully opened , sir")
        elif 'open teams' in query:
            codePath = "C:\\Users\\raush\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
            os.startfile(codePath)
            speak("Successfully opened , sir")
        elif 'email to me' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "raushangupta2231@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(a)
                speak("Sorry sir, unable to send email")
        elif 'stop' in query:
            speak("Okay,Bye sir, hope so we will meet soon")
            quit(0)
        elif 'send message' in query:

            # speak("what is hours")
            # hours= takeCommand()
            # speak("what is the mintues")
            # minutes= takeCommand()
            # print(f"sir,you want to send message at {hours} hours and {minutes}")
            # speak(f"sir,you want to send message at {hours} hours and {minutes}")
            speak("what should i say")
            content = takeCommand()
            pywhatkit.sendwhatmsg('+91 999999999', content, 23, 24)

        elif 'close laptop' in query:
            speak("sir, please confirm you want to shut down or not")
            m=takeCommand()
            
            if(m=="Yes".lower()):
                speak("shutting down")
                os.system('shutdown -s')
                exit()
            elif(m=="No".lower()):
                speak("okay sir continue")
                exit()
        
 
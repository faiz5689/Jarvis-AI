from datetime import datetime
from tkinter import E
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am your Computer AI. Ready to serve you.")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-us')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    
    return query


if __name__ == "__main__":
    wishME()
    
    while True:
        query = 'play music'

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wkikpedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
            
        elif 'play music' in query:
            webbrowser.open('https://www.youtube.com/watch?v=koeObMIFBjg')
            
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open email' in query:
            webbrowser.open("gmail.com")
        elif 'open emails' in query:
            webbrowser.open("gmail.com")
            
        elif 'email to' in query:
            try:
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
            except Exception as e:
                speak("couldn't open email")
            
        elif 'quit' in query:
            speak("Goodbye! Hope to meet again")
            exit
        
        else:
            speak("Not sure what to do with the command")
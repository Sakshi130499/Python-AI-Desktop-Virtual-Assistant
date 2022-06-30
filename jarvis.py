from pip import main
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import subprocess as sp
import pywhatkit as kit

paths = {
    'notepad': "C:\\Windows\\system32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"  
}

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices) //Male,Female voice print

engine.setProperty('voice',voices[0].id)
# print(voices[0].id)   male
# print(voices[1].id)   female


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("hello Sir. Please tell me how may I help you") 

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...") 
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    
    while True:
        query= takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Seaching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak('According to Wikipedia...')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chandigarh university website' in query:
            webbrowser.open("https://uims.cuchd.in/")

        elif 'play music' in query:
            # using random module to play music
            music_dir = 'F:\\sakshi study\\Python Project\\music\\'
    
            dict1 = {
                '1' : 'Love You Zindagi.mp3',
                '2' : 'Tum Hi Ho Bandhu.mp3',
                '3' : 'Sooraj Ki Baahon Mein.mp3',
                '4' : 'Ilahi.mp3'
            }
            key = random.choice(list(dict1.keys()))
            os.startfile(os.path.join(music_dir,dict1[key]))          

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            os.startfile(paths['notepad']) 

        elif 'open calculator' in query:
            os.startfile(paths['calculator'])    
        
        elif 'open camera' in query:
            sp.run('start microsoft.windows.camera:', shell=True)

        elif 'open command prompt' in query:
             os.system('start cmd')

        elif 'play youtube video' in query:
            video = takeCommand()
            kit.playonyt(video)
        
        elif 'send whatsapp message' in query:
            kit.sendwhatmsg_instantly(f"+91{8954868081}", 'hello Akash Vats')


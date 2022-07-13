import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  #for using inbuit voices of windows
voices=engine.getProperty('voices')
 #print(voices[0].id)
engine.setProperty('voice', voices[1].id)  #voice ki property set kr rhhe ki male or female


def speak(audio):
    engine.say(audio)  #'audio' ko engine bolega 
    engine.runAndWait()  # pause between two events

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Shadan")
    elif hour>=12 and hour<18:
        speak("Good Afternoon shadan")
    else:
        speak("Good evening shadan")

    speak("How may i assist you")    


def takeCommand():
    #it takes microphone input and return string as o/p
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said:- {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"    
    return query


if __name__ == "__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()  # lower case string mein change

        #Logic for executing tasks vased on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("wikipedia according to jarvis")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            music_dir='C:\\music'     
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\\91998\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    




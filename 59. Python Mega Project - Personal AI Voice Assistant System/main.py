import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser
import wikipedia
import subprocess
import random 


# This is Logger for the application
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR, exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)



#Taking the male voice from my system
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


def speak(text):
    """This function converts text to a voice

    Args:
        text
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()





def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    return query


#this function will wish you
def wish_me():
    hour = (datetime.datetime.now().hour)
    
    if hour >=0 and hour <=12:
        speak("Good Morning sir! How are you doing?")
    
    elif hour >=12 and hour <=18:
        speak("Good afternoon sir! How are you doing?")
    
    else:
        speak("Good evening sir! How are you doing?")
    
    speak("I am JARVIS.Tell me sir how can i help you?")



def play_music():
    music_dir = "D:\\Bappy\\Coding\\Youtube\\Python Tutorials\\Mega Projects\\JARVIS-System\\music"   # <-- change this to your music folder
    try:
        songs = os.listdir(music_dir)
        if songs:
            random_song = random.choice(songs)
            speak(f"Playing a random song sir: {random_song}")
            os.startfile(os.path.join(music_dir, random_song))
        else:
            speak("No music files found in your music directory.")
    except Exception:
        speak("Sorry sir, I could not find your music folder.")



wish_me()
while True:

    query = takeCommand().lower()
    print(query)
    
    if "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")

    
    elif "name" in query:
        print("I am in name")
        speak("My name is JARVIS")

    
    # Small talk
    elif "how are you" in query:
        speak("I am functioning at full capacity sir!")

    
    elif "who made you" in query:
        speak("I was created by Bappy sir, a brilliant mind!")

    
    elif "thank you" in query:
        speak("It's my pleasure sir. Always happy to help.")


    
    elif "play music" in query or "music" in query:
        play_music()

    
    elif "exit" in query:
        speak("Good bye sir")
        exit()

    
    # Calculator
    elif "open calculator" in query or "calculator" in query:
        speak("Opening calculator")
        subprocess.Popen("calc.exe")

    
     # Notepad
    elif "open notepad" in query:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")


    elif "open google" in query:
        speak("ok sir. please type here what do you want to read")
        webbrowser.open("google.com")

    
    # Command Prompt
    elif "open terminal" in query or "open cmd" in query:
        speak("Opening Command Prompt terminal")
        subprocess.Popen("cmd.exe")

    
    # Calendar
    elif "open calendar" in query or "calendar" in query:
        speak("Opening Windows Calendar")
        webbrowser.open("https://calendar.google.com")

    
    # Jokes
    elif "joke" in query:
        jokes = [
            "Why don't programmers like nature? Too many bugs.",
            "I told my computer I needed a break. It said no problem, it will go to sleep.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))

    
    # YouTube search
    elif "youtube" in query:
        speak("Opening YouTube for you.")
        query = query.replace("youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    
    elif "open facebook" in query:
        speak("ok sir. opening facebook")
        webbrowser.open("facebook.com")

    
    #This query for search something from wikipedia
    elif 'wikipedia' in query:
        speak("Searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia ")
        print(results)
        speak(results)





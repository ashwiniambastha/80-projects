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

speak("hey gandu, kaisa hain behen")
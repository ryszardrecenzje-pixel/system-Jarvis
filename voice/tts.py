# voice/tts.py
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 180)
engine.setProperty("volume", 1.0)

def speak(text: str):
    engine.say(text)
    engine.runAndWait()

# voice/stt.py
import speech_recognition as sr

def listen_to_microphone() -> str:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Jarvis nasłuchuje...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="pl-PL")
        return text
    except Exception as e:
        return f"Błąd rozpoznawania mowy: {e}"

# app.py
import streamlit as st
from ui.layout import render_main_ui
from core.ai import handle_user_input
from voice.stt import listen_to_microphone
from voice.tts import speak
import os

if os.getenv("STREAMLIT_RUNTIME"):
    print("Uruchamiam wersję chmurową — bez PyAudio")
else:
    print("Uruchamiam wersję lokalną — pełny Jarvis z audio")


def main():
    st.set_page_config(page_title="Jarvis", layout="wide")
    st.title("Jarvis – asystent kodowania")

    user_input = render_main_ui()

    # Obsługa trybu głosowego
    if user_input == "__voice_listen__":
        st.write("Nasłuchuję...")
        text = listen_to_microphone()
        st.write(f"Usłyszałem: {text}")
        response = handle_user_input(text)
        speak(response)
        st.write("### Odpowiedź Jarvisa:")
        st.write(response)
        return

    if user_input:
        response = handle_user_input(user_input)
        speak(response)  # Jarvis mówi odpowiedź
        st.markdown("### Odpowiedź Jarvisa:")
        st.write(response)


if __name__ == "__main__":
    main()

# ui/layout.py
import streamlit as st

def render_main_ui():
    st.sidebar.header("Tryby Jarvisa")

    mode = st.sidebar.radio(
        "Wybierz tryb:",
        ["Chat", "Kodowanie", "Streamlit", "GitHub", "System", "Pamięć", "Głos"]
    )

    st.subheader(f"Tryb: {mode}")

    if mode == "Chat":
        return render_chat_mode()

    if mode == "Kodowanie":
        return render_code_mode()

    if mode == "Streamlit":
        return render_streamlit_mode()

    if mode == "GitHub":
        return render_github_mode()

    if mode == "System":
        return render_system_mode()

    if mode == "Pamięć":
        return render_memory_mode()

    if mode == "Głos":
        return render_voice_mode()

    return None


def render_chat_mode():
    st.write("Konwersacja z Jarvisem")
    user_input = st.text_area("Twoje polecenie:", height=120)
    if st.button("Wyślij"):
        return user_input
    return None


def render_code_mode():
    st.write("Generowanie kodu Python")
    filename = st.text_input("Nazwa pliku:")
    content = st.text_area("Zawartość pliku:")
    if st.button("Stwórz plik"):
        return f"stwórz plik {filename} {content}"
    return None


def render_streamlit_mode():
    st.write("Tworzenie aplikacji Streamlit")
    name = st.text_input("Nazwa aplikacji:")
    if st.button("Generuj aplikację"):
        return f"stwórz aplikację streamlit {name}"
    return None


def render_github_mode():
    st.write("Operacje GitHub")
    if st.button("Commit"):
        return "commit"
    if st.button("Push"):
        return "push"
    return None


def render_system_mode():
    st.write("Tryb systemowy")

    action = st.selectbox("Wybierz akcję:", [
        "Pokaż katalog",
        "Stwórz folder",
        "Usuń plik",
        "Odczytaj plik",
        "Zapisz plik"
    ])

    path = st.text_input("Ścieżka:")

    content = ""
    if action == "Zapisz plik":
        content = st.text_area("Zawartość pliku:")

    if st.button("Wykonaj"):
        if action == "Pokaż katalog":
            return f"pokaż katalog {path}"
        if action == "Stwórz folder":
            return f"stwórz folder {path}"
        if action == "Usuń plik":
            return f"usuń plik {path}"
        if action == "Odczytaj plik":
            return f"odczytaj plik {path}"
        if action == "Zapisz plik":
            return f"zapisz plik {path} {content}"

    return None



def render_memory_mode():
    st.write("Pamięć Jarvisa")
    key = st.text_input("Klucz pamięci:")
    value = st.text_area("Wartość:")
    if st.button("Zapamiętaj"):
        return f"zapamiętaj {key} {value}"
    if st.button("Przypomnij"):
        return f"przypomnij {key}"
    return None


def render_voice_mode():
    st.write("Tryb głosowy Jarvisa")

    if st.button("Nasłuchuj"):
        return "__voice_listen__"

    st.write("Jarvis będzie mówił odpowiedzi automatycznie.")
    return None


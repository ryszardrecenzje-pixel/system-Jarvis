# ui/layout.py
import streamlit as st

def render_docs_mode():
    st.write("Moduł dokumentacji")

    action = st.selectbox("Wybierz akcję:", [
        "Generuj README",
        "Dokumentacja repozytorium",
        "Raport techniczny aplikacji",
        "Sugestia workflow"
    ])

    app_name = ""
    description = ""

    if action == "Generuj README":
        app_name = st.text_input("Nazwa aplikacji:")
        description = st.text_area("Opis aplikacji:")

    if action == "Raport techniczny aplikacji":
        app_name = st.text_input("Nazwa aplikacji:")

    if st.button("Wykonaj"):
        if action == "Generuj README":
            return f"readme {app_name} {description}"
        if action == "Dokumentacja repozytorium":
            return "struktura repo"
        if action == "Raport techniczny aplikacji":
            return f"raport techniczny {app_name}"
        if action == "Sugestia workflow":
            return "workflow"

    return None


def render_workflow_mode():
    st.write("Inteligentny Workflow Jarvisa")

    action = st.selectbox("Wybierz akcję:", [
        "Analiza projektu",
        "Generuj workflow"
    ])

    user_input = st.text_area("Polecenie użytkownika:")

    if st.button("Wykonaj"):
        if action == "Analiza projektu":
            return "analiza projektu"
        if action == "Generuj workflow":
            return f"workflow {user_input}"

    return None


def render_main_ui():
    st.sidebar.header("Tryby Jarvisa")

    mode = st.sidebar.radio(
        "Wybierz tryb:",
        ["Chat", "Workflow", "Kodowanie", "Streamlit", "GitHub", "System", "Pamięć", "Głos", "Analiza danych", "Dokumentacja"]

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
   
    if mode == "Analiza danych":
        return render_data_mode()

    if mode == "Dokumentacja":
        return render_docs_mode()
    
    if mode == "Workflow":
        return render_workflow_mode()

    

    return None
def render_data_mode():
    st.write("Analiza danych")

    action = st.selectbox("Wybierz akcję:", [
        "Wczytaj CSV",
        "Wczytaj JSON",
        "Wczytaj Excel",
        "Statystyki danych",
        "Wykres kolumny"
    ])

    path = st.text_input("Ścieżka do pliku:")

    column = ""
    if action == "Wykres kolumny":
        column = st.text_input("Nazwa kolumny:")

    if st.button("Wykonaj"):
        if action == "Wczytaj CSV":
            return f"wczytaj csv {path}"
        if action == "Wczytaj JSON":
            return f"wczytaj json {path}"
        if action == "Wczytaj Excel":
            return f"wczytaj excel {path}"
        if action == "Statystyki danych":
            return "statystyki"
        if action == "Wykres kolumny":
            return f"wykres {column}"

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
    st.write("Zarządzanie aplikacjami Streamlit")

    action = st.selectbox("Wybierz akcję:", [
        "Lista aplikacji",
        "Stwórz aplikację",
        "Modyfikuj aplikację",
        "Generuj dashboard"
    ])

    name = st.text_input("Nazwa aplikacji:")

    new_code = ""
    if action == "Modyfikuj aplikację":
        new_code = st.text_area("Nowy kod aplikacji:")

    if st.button("Wykonaj"):
        if action == "Lista aplikacji":
            return "lista aplikacji"
        if action == "Stwórz aplikację":
            return f"stwórz aplikację {name}"
        if action == "Modyfikuj aplikację":
            return f"modyfikuj aplikację {name} {new_code}"
        if action == "Generuj dashboard":
            return f"dashboard {name}"

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


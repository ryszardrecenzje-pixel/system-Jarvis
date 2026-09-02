# actions/streamlit_apps.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APPS_DIR = os.path.join(BASE_DIR, "streamlit_apps")

def list_apps():
    if not os.path.exists(APPS_DIR):
        return "Brak folderu streamlit_apps."

    apps = os.listdir(APPS_DIR)
    if not apps:
        return "Brak aplikacji Streamlit."

    return "Dostępne aplikacje:\n" + "\n".join(apps)


def create_app(name: str):
    app_path = os.path.join(APPS_DIR, name)
    os.makedirs(app_path, exist_ok=True)

    content = f"""
import streamlit as st

st.title("{name} – aplikacja wygenerowana przez Jarvisa")
st.write("To jest automatycznie wygenerowana aplikacja Streamlit.")
"""

    file_path = os.path.join(app_path, "app.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Utworzono aplikację Streamlit: {file_path}"


def modify_app(name: str, new_code: str):
    file_path = os.path.join(APPS_DIR, name, "app.py")

    if not os.path.exists(file_path):
        return f"Aplikacja {name} nie istnieje."

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_code)

    return f"Zaktualizowano aplikację: {file_path}"


def generate_dashboard(name: str, df):
    app_path = os.path.join(APPS_DIR, name)
    os.makedirs(app_path, exist_ok=True)

    content = f"""
import streamlit as st
import pandas as pd

st.title("Dashboard: {name}")
st.write("Automatycznie wygenerowany dashboard Jarvisa.")

df = pd.DataFrame({df.to_dict()})

st.subheader("Podgląd danych")
st.dataframe(df)

st.subheader("Statystyki")
st.write(df.describe())

st.subheader("Wykres")
st.line_chart(df)
"""

    file_path = os.path.join(app_path, "app.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Dashboard wygenerowany: {file_path}"

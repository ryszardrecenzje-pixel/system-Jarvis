# actions/codegen.py
import os
from datetime import datetime

def create_python_file(path: str, content: str) -> str:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return f"Plik Python został utworzony: {path}"

def append_to_file(path: str, content: str) -> str:
    if not os.path.exists(path):
        return f"Plik {path} nie istnieje."

    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + content)

    return f"Dodano kod do pliku: {path}"

def generate_streamlit_app(name: str) -> tuple[str, str]:
    filename = f"streamlit_apps/{name}/app.py"
    content = f"""
import streamlit as st

st.title("{name} – aplikacja wygenerowana przez Jarvisa")
st.write("To jest automatycznie wygenerowana aplikacja Streamlit.")
"""

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename, content

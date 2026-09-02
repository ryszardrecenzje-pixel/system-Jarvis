# actions/data_analysis.py
import pandas as pd
import json
import streamlit as st

def load_csv(path: str):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        return f"Błąd wczytywania CSV: {e}"

def load_json(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        return f"Błąd wczytywania JSON: {e}"

def load_excel(path: str):
    try:
        df = pd.read_excel(path)
        return df
    except Exception as e:
        return f"Błąd wczytywania Excel: {e}"

def describe_dataframe(df):
    try:
        return df.describe(include="all")
    except Exception as e:
        return f"Błąd analizy danych: {e}"

def plot_column(df, column: str):
    try:
        fig = df[column].plot(kind="bar", figsize=(10, 4))
        st.pyplot(fig.figure)
        return f"Wygenerowano wykres kolumny: {column}"
    except Exception as e:
        return f"Błąd generowania wykresu: {e}"

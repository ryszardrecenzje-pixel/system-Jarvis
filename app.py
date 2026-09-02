# app.py
import streamlit as st
from ui.layout import render_main_ui
from core.ai import handle_user_input

def main():
    st.set_page_config(page_title="Jarvis", layout="wide")
    st.title("Jarvis – asystent kodowania")

    user_input = render_main_ui()

    if user_input:
        response = handle_user_input(user_input)
        st.markdown("### Odpowiedź Jarvisa:")
        st.write(response)

if __name__ == "__main__":
    main()

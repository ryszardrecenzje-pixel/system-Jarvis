# ui/layout.py
import streamlit as st

def render_main_ui():
    st.sidebar.header("Sterowanie")
    st.sidebar.write("Tu później dodamy tryby: kodowanie, GitHub, Streamlit, głos itd.")

    st.subheader("Konwersacja z Jarvisem")
    user_input = st.text_area("Twoje polecenie:", height=120)

    if st.button("Wyślij do Jarvisa"):
        return user_input

    return None

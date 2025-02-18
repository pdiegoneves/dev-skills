import streamlit as st

def question(question:str, response:str):
    with st.expander(question):
        st.text(response)
import streamlit as st
from helper import Helper
from pages.Login import authenticator


st.title("Welcome to Data Verify Center")

if not Helper.get_authen_status():
    st.warning("Please login first!")
    st.stop()

st.write(f"## Hi, {st.session_state['name']}")


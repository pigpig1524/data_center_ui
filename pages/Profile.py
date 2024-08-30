import streamlit as st
from pages.Login import authenticator

name, authentication_status, username = authenticator.login(location="unrendered")


st.title("Try new feature")
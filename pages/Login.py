import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import time

# Cofig user details at users.yaml, se toml format in the future
with open('./users.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    # config['preauthorized']
)

name, authentication_status, username = authenticator.login()

if st.session_state['authentication_status'] is True:
    st.success("Login successfully!")
    time.sleep(1)
    st.rerun(scope="app")
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')


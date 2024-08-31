import streamlit as st
from pages.Login import authenticator
import time


# # @st.dialog("Are you sure to log out?")
# # def log_out_sure():
# #     # st.write("Log out in th next 2 seconds...")
# #     if st.button("Sure"):
# #         authenticator.logout(location="unrendered")
# #     else:
# #         return False


# # time.sleep(2)

# st.write(f"Are you sure to logout, {st.session_state['name']}?")

# yes_button = st.button("Yes", key="sure_to_logout")
# no_button = st.button("No", key="not_sure_to_logout")

# if yes_button:
#     authenticator.logout(location="unrendered")
# elif no_button:
#     st.switch_page("pages/Home.py")
# # st.rerun(scope='app')

# Make the dialog for user confirm logout request
# This function use 'sure_to_logout' key in session_state

def logout_sure():
    st.session_state['sure_to_logout'] = True

def logout_not_sure():
    st.session_state['sure_to_logout'] = False

@st.dialog("Are you sure to log out?")
def logout_confirm():
    yes_button = st.button("Yes", on_click=logout_sure)
    no_button = st.button("No", on_click=logout_not_sure)
    if yes_button or no_button:
        st.rerun()


# If user confirm sure to log out, the app wwil execute log out without render the og out button
# Else, switch to the home page

if 'sure_to_logout' not in st.session_state:
    logout_confirm()
elif st.session_state['sure_to_logout']:
    authenticator.logout(location="unrendered")
    del st.session_state['sure_to_logout']
else:
    del st.session_state['sure_to_logout']
    st.switch_page("pages/Home.py")

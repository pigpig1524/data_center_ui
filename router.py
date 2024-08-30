import streamlit as st
from pages.Login import authenticator
from streamlit_option_menu import option_menu
from helper import Helper

login_page = st.Page("pages/Login.py", title="Login", icon=":material/login:")
logout_page = st.Page("pages/Logout.py", title="Logout", icon=":material/logout:")
home_page = st.Page("pages/Home.py", title="Home",icon=":material/home:", default=True)
tasks_page = st.Page("pages/Tasks.py", title="Your tasks", icon=":material/task:")



if Helper.get_authen_status():
    # profile_page = st.Page("pages/Profile.py", title=f"Hi, {st.session_state['name']}", icon=":material/person:")
    pg = st.navigation(
        pages={
            "Account": [logout_page],
            "Dashboard": [home_page, tasks_page]
        }
    )
else:
    pg = st.navigation(
        pages={
            "Account": [login_page],
            "Dashboard": [home_page]
        }
    )

pg.run()

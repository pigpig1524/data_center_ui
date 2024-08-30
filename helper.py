import streamlit as st

class Helper:
    def __init__(self) -> None:
        pass

    
    def get_authen_status() -> bool:
        try:
            return st.session_state.authentication_status
        except:
            return False
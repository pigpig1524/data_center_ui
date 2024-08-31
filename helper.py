import streamlit as st

class Helper:
    def __init__(self) -> None:
        pass

    
    def get_authen_status() -> bool:
        """
        To get the login status
        Args: none
        Output:
            (bool): True if logged in successfully and False for the other case
        """

        try:
            return st.session_state.authentication_status
        except:
            return False
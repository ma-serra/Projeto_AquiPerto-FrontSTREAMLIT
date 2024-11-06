# utils.py

import streamlit as st

def initialize_session():
    """
    Inicializa as variáveis de estado da sessão.
    """
    if 'user_email' not in st.session_state:
        st.session_state['user_email'] = None

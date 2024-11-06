# app.py

import streamlit as st
from utils import initialize_session
from pages.login import login_page
from pages.cadastro import cadastro_page
from pages.home import home_page  # Import the home_page function

def main():
    # Initialize session state
    initialize_session()

    # Page configuration
    st.set_page_config(page_title="Aqui Perto", page_icon="🏠", layout="centered")

    # Initialize the current page in session_state
    if 'page' not in st.session_state:
        st.session_state.page = 'inicio'  # Start at the 'inicio' page

    # Sidebar with navigation buttons
    with st.sidebar:
        st.title("Menu de Navegação")

        # If user is not logged in, show Login and Cadastro buttons
        if st.session_state.user_email is None:
            if st.button("Login"):
                st.session_state.page = 'login'
            if st.button("Cadastro"):
                st.session_state.page = 'cadastro'
        else:
            # If user is logged in, show Logout button and navigation to Home
            st.write(f"Usuário: {st.session_state.user_email}")
            if st.button("Home"):
                st.session_state.page = 'home'
            if st.button("Logout"):
                st.session_state.user_email = None
                st.session_state.page = 'inicio'
                st.rerun()  # Reload the app to update the page

    # Display content based on the current page
    if st.session_state.page == "inicio":
        st.title("Bem-vindo ao Aqui Perto")
        st.write("Selecione uma opção no menu lateral.")
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "cadastro":
        cadastro_page()
    elif st.session_state.page == "home":
        home_page()
    else:
        st.error("Página não encontrada.")
        st.session_state.page = 'inicio'

if __name__ == "__main__":
    main()

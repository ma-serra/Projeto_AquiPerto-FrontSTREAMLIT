# pages/home.py

import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from utils import initialize_session

def home_page():
    # Initialize session state
    initialize_session()

    # Verify if the user is logged in
    if st.session_state.user_email is None:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state.page = 'login'
        st.rerun()  # Reload the app to update the page
        return

    # Function to encode image in base64 for HTML display
    def encode_image(image_path):
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            return encoded_string
        except FileNotFoundError:
            st.error("Logo não encontrada.")
            return ""

    # Function to display the centered logo with adjustable margins
    def display_centered_logo(image_path, width=200, top_margin="-200px", bottom_margin="-200px"):
        encoded_image = encode_image(image_path)
        if encoded_image:
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center; height: 60vh; margin-top: {top_margin}; margin-bottom: {bottom_margin};">
                    <img src="data:image/png;base64,{encoded_image}" width="{width}">
                </div>
                """,
                unsafe_allow_html=True
            )

    def botoes_sidebar():
        # CSS styling for buttons and section titles
        st.sidebar.markdown("""
        <style>
        /* Style for section titles */
        .section-title {
            font-size: 18px;
            margin-top: 20px;
            margin-bottom: 10px;
            color: #333333;
            font-weight: bold;
        }

        /* Style for sidebar buttons */
        .sidebar-button {
            display: block;
            width: 100%;
            height: 40px;
            line-height: 40px;
            font-size: 16px;
            font-family: sans-serif;
            text-decoration: none;
            color: #333;
            border: 2px solid #333;
            letter-spacing: 1px;
            text-align: center;
            position: relative;
            transition: all 0.35s;
            margin-bottom: 10px;
            border-radius: 5px;
            background-color: transparent;
        }

        .sidebar-button:hover {
            color: #fff;
            background-color: #333;
        }
        </style>
        """, unsafe_allow_html=True)

        # First section: Account (Logout)
        st.sidebar.markdown("<div class='section-title'>Conta</div>", unsafe_allow_html=True)
        if st.sidebar.button("Logout", key="logout_button"):
            st.session_state.user_email = None
            st.session_state.page = 'inicio'
            st.experimental_rerun()  # Reload the app

        # Second section: Navigation (Serviços, Favoritos, Mapa)
        st.sidebar.markdown("<div class='section-title'>Navegação</div>", unsafe_allow_html=True)
        if st.sidebar.button("Serviços"):
            st.session_state.page = 'servicos'
            st.experimental_rerun()
        if st.sidebar.button("Favoritos"):
            st.session_state.page = 'favoritos'
            st.experimental_rerun()
        if st.sidebar.button("Mapa"):
            st.session_state.page = 'mapa'
            st.experimental_rerun()

    botoes_sidebar()

    # Display welcome message with user's email
    st.write(f"Bem-vindo, {st.session_state.get('user_email', 'usuário')}!")

    # Center the logo in the main area
    logo_path = 'img/logo_aqui_perto.png'
    display_centered_logo(logo_path, width=200)

    # Load and display the Home page content
    try:
        with open("templates/home.html", "r", encoding="utf-8") as file:
            html_code = file.read()
        components.html(html_code, width=None, height=920, scrolling=False)
    except FileNotFoundError:
        st.error("O arquivo 'home.html' não foi encontrado na pasta 'templates'.")

import streamlit as st
import streamlit.components.v1 as components
import base64
from utils import initialize_session

def home_page():

    initialize_session()

    if st.session_state.user_email is None:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state.page = 'login'
        st.rerun()
        return

    def encode_image(image_path):
        try:
            with open(image_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            return encoded_string
        except FileNotFoundError:
            st.error("Logo não encontrada.")
            return ""

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

    logo_path = 'img/logo_aqui_perto.png'
    display_centered_logo(logo_path, width=200)

    try:
        with open("templates/home.html", "r", encoding="utf-8") as file:
            html_code = file.read()
        components.html(html_code, width=None, height=920, scrolling=False)
    except FileNotFoundError:
        st.error("O arquivo 'home.html' não foi encontrado na pasta 'templates'.")

import streamlit as st
import requests

api_url = "http://127.0.0.1:5000/home"

# Código da home page aqui

st.markdown(
    """
    <a href="/mapa" target="_self">
        <button style="display:block; width:200px; height:50px;">
            Ir para a próxima página
        </button>
    </a>
    """,
    unsafe_allow_html=True
)
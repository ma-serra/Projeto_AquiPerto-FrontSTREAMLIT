# pages/cadastro.py

import streamlit as st
import requests
from utils import initialize_session

def cadastro_page():
    # Initialize session state
    initialize_session()

    st.title("Cadastro")

    nome = st.text_input("Nome")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type='password')

    if st.button("Cadastrar"):
        if nome and email and senha:
            data = {'nome': nome, 'email': email, 'senha': senha}
            try:
                response = requests.post("http://localhost:5000/usuarios", json=data)
                # Check if the response is successful
                if response.status_code == 201:
                    st.success("Cadastro realizado com sucesso! Você pode agora fazer login.")
                    st.session_state.page = 'login'  # Redirect to login.py
                    st.experimental_rerun()  # Reload the app to update the page
                    return
                else:
                    error_message = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Erro no cadastro: {error_message}")
            except Exception as e:
                st.error(f"Erro ao conectar com o servidor: {e}")
        else:
            st.warning("Por favor, preencha todos os campos.")

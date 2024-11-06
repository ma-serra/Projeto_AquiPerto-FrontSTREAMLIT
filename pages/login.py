import streamlit as st
import requests
from utils import initialize_session

def login_page():

    initialize_session()

    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type='password')

    if st.button("Entrar"):
        if email and senha:
            data = {'email': email, 'senha': senha}
            try:
                response = requests.post("http://localhost:5000/login", json=data)
                if response.status_code == 200:
                    st.success("Login realizado com sucesso!")
                    st.session_state['user_email'] = email
                    st.session_state.page = 'home'
                    st.rerun()
                    return
                else:
                    error_message = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Erro no login: {error_message}")
            except Exception as e:
                st.error(f"Erro ao conectar com o servidor: {e}")
        else:
            st.warning("Por favor, preencha todos os campos.")

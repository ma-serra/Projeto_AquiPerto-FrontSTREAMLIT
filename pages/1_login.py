import streamlit as st
import requests
import os

# URL do backend Flask
API_URL = "http://localhost:5000"

# Exibir o logo
if os.path.exists("img/logo.png"):
    st.image("img/logo.png", width=200)

st.title("Login")

email = st.text_input("Email")
senha = st.text_input("Senha", type='password')

if st.button("Entrar"):
    if email and senha:
        data = {'email': email, 'senha': senha}
        try:
            response = requests.post(f"{API_URL}/login", json=data)
            if response.status_code == 200:
                st.success("Login realizado com sucesso!")
                st.session_state['logged_in'] = True
                st.session_state['user_email'] = email
                # Redirecionar para a página Home
                st.markdown("<meta http-equiv='refresh' content='0; url=/' />", unsafe_allow_html=True)
            else:
                error_message = response.json().get('erro', 'Erro desconhecido.')
                st.error(f"Erro no login: {error_message}")
        except Exception as e:
            st.error(f"Erro ao conectar com o servidor: {e}")
    else:
        st.warning("Por favor, preencha todos os campos.")

# Área após login
if 'logged_in' in st.session_state and st.session_state['logged_in']:
    # Usuário já está logado, redirecionar para a Home
    st.markdown("<meta http-equiv='refresh' content='0; url=/' />", unsafe_allow_html=True)

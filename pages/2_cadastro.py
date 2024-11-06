import streamlit as st
import requests
from time import sleep

API_URL = "http://localhost:5000"

st.title("Aplicativo de Cadastro")

st.subheader("Cadastro")

nome = st.text_input("Nome Completo")
email = st.text_input("Email")
senha = st.text_input("Senha", type='password')
confirmar_senha = st.text_input("Confirmar Senha", type='password')

if st.button("Cadastrar"):
    if nome and email and senha and confirmar_senha:
        if senha != confirmar_senha:
            st.error("As senhas não coincidem.")
        else:
            data = {
                'nome': nome,
                'email': email,
                'senha': senha,
                'confirmar_senha': confirmar_senha
            }
            try:
                response = requests.post(f"{API_URL}/usuarios", json=data)
                if response.status_code == 201:
                    st.success("Cadastro realizado com sucesso! Por favor, faça login.")
                    st.session_state['logou'] = True
                elif response.status_code == 409:
                    error_message = response.json().get('erro', 'Email já cadastrado.')
                    st.error(f"Erro no cadastro: {error_message}")
                elif response.status_code == 400:
                    error_message = response.json().get('erro', 'Erro no cadastro.')
                    st.error(f"Erro no cadastro: {error_message}")
                else:
                    error_message = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Erro no cadastro: {error_message}")
            except requests.exceptions.JSONDecodeError:
                st.error("Erro ao decodificar a resposta do servidor.")
            except Exception as e:
                st.error(f"Erro ao conectar com o servidor: {e}")
    else:
        st.warning("Por favor, preencha todos os campos.")

if 'logou' in st.session_state and st.session_state['logou']:
    sleep(1.3)
    st.switch_page('pages/1_login.py')
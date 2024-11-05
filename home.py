import streamlit as st
import requests
import streamlit.components.v1 as components
import os

def center_logo_and_buttons():
    # Cria três colunas para centralizar o conteúdo na coluna do meio
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        # Exibir a logo se o arquivo existir
        if os.path.exists('img/logo_aqui_perto.png'):
            st.image('img/logo_aqui_perto.png', width=200)
        else:
            st.write('Logo não encontrada.')

        # Espaçamento
        st.write("")

        # Verificar se o usuário está logado
        if 'logged_in' in st.session_state and st.session_state['logged_in']:
            # Usuário está logado
            st.write(f"Bem-vindo, {st.session_state.get('user_email', '')}!")

            if st.button("Sair"):
                st.session_state.clear()
                # Redirecionar para a Home após logout
                st.markdown("<meta http-equiv='refresh' content='0; url=/' />", unsafe_allow_html=True)
        else:
            # Usuário não está logado, exibir botões de Login e Cadastro
            if st.button('Login'):
                # Redirecionar para a página de login
                st.markdown("<meta http-equiv='refresh' content='0; url=/login' />", unsafe_allow_html=True)
            if st.button('Cadastro'):
                # Redirecionar para a página de cadastro
                st.markdown("<meta http-equiv='refresh' content='0; url=/cadastro' />", unsafe_allow_html=True)

# Centralizar a logo e os botões
center_logo_and_buttons()

# Carregar e exibir o conteúdo da página Home
with open("templates/home.html", "r", encoding="utf-8") as file:
    html_code = file.read()

components.html(html_code, width=None, height=1025, scrolling=False)
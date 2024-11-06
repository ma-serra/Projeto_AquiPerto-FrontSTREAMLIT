# app.py

import streamlit as st
from utils import initialize_session
from pages.login import login_page
from pages.cadastro import cadastro_page
from pages.home import home_page
from pages.servicos import servicos_page
# Importar outras páginas conforme necessário

def main():
    # Configuração da página (deve ser o primeiro comando Streamlit)
    st.set_page_config(page_title="Aqui Perto", page_icon="🏠", layout="centered")

    # Inicialização do estado de sessão
    initialize_session()

    # Inicializa a página atual no session_state
    if 'page' not in st.session_state:
        st.session_state.page = 'inicio'

    # Adiciona botões de navegação na sidebar
    with st.sidebar:
        st.title("Menu de Navegação")

        # Se o usuário não estiver logado, mostrar opções de Login e Cadastro
        if st.session_state.user_email is None:
            if st.button("Login", key="sidebar_login"):
                st.session_state.page = 'login'
                st.rerun()
            if st.button("Cadastro", key="sidebar_cadastro"):
                st.session_state.page = 'cadastro'
                st.rerun()
        else:
            # Se o usuário estiver logado, mostrar opções de navegação e Logout
            st.write(f"Usuário: {st.session_state.user_email}")
            if st.button("Home", key="sidebar_home"):
                st.session_state.page = 'home'
                st.rerun()
            if st.button("Serviços", key="sidebar_servicos"):
                st.session_state.page = 'servicos'
                st.rerun()
            if st.button("Logout", key="sidebar_logout"):
                st.session_state.user_email = None
                st.session_state.page = 'inicio'
                st.rerun()

    # Condicional para exibir conteúdo baseado na página atual
    if st.session_state.page == "inicio":
        st.title("Bem-vindo ao Aqui Perto")
        st.write("Selecione uma opção no menu lateral.")
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "cadastro":
        cadastro_page()
    elif st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "servicos":
        servicos_page()
    # Incluir outras páginas conforme necessário
    else:
        st.error("Página não encontrada.")
        st.session_state.page = 'inicio'

if __name__ == "__main__":
    main()

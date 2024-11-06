import streamlit as st
from utils import initialize_session
from pages.login import login_page
from pages.cadastro import cadastro_page
from pages.home import home_page
from pages.servicos import servicos_page
from pages.mapa import mapa_page
from pages.favoritos import favoritos_page

def main():
    st.set_page_config(page_title="Aqui Perto", page_icon="🏠", layout="centered")
    initialize_session()
    if 'page' not in st.session_state:
        st.session_state.page = 'inicio'

    st.markdown("""
    <style>
    /* Estilo para os botões na barra lateral */
    [data-testid="stSidebar"] .stButton > button {
        background-color: #333333;
        color: #ffffff !important; /* Garante que o texto seja sempre branco */
        width: 100%;
        height: 40px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        margin: 5px 0;
    }

    /* Estilo para o estado hover dos botões na barra lateral */
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #555555;
        color: #ffffff !important; /* Garante que o texto permaneça branco ao passar o mouse */
    }

    /* Garante que todos os elementos internos do botão também tenham texto branco */
    [data-testid="stSidebar"] .stButton > button * {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("Menu de Navegação")
        if st.session_state.user_email is None:
            if st.button("Login", key="sidebar_login"):
                st.session_state.page = 'login'
                st.rerun()
            if st.button("Cadastro", key="sidebar_cadastro"):
                st.session_state.page = 'cadastro'
                st.rerun()
        else:
            st.write(f"Usuário: {st.session_state.user_email}")
            if st.button("Home", key="sidebar_home"):
                st.session_state.page = 'home'
                st.rerun()
            if st.button("Serviços", key="sidebar_servicos"):
                st.session_state.page = 'servicos'
                st.rerun()
            if st.button("Mapa", key="sidebar_mapa"):
                st.session_state.page = 'mapa'
                st.rerun()
            if st.button("Favoritos", key="sidebar_favoritos"):
                st.session_state.page = 'favoritos'
                st.rerun()
            if st.button("Logout", key="sidebar_logout"):
                st.session_state.user_email = None
                st.session_state.page = 'inicio'
                st.rerun()

    # Função para exibir a logo centralizada
    def exibir_logo():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("img/logo_aqui_perto.png", width=200)

    if st.session_state.page == "inicio":
        exibir_logo()
        st.title("Bem-vindo ao Aqui Perto")
        st.write("Selecione uma opção no menu lateral.")

    elif st.session_state.page == "login":
        exibir_logo()
        login_page()
    elif st.session_state.page == "cadastro":
        exibir_logo()
        cadastro_page()
    elif st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "servicos":
        servicos_page()
    elif st.session_state.page == "mapa":
        exibir_logo()
        mapa_page()
    elif st.session_state.page == "favoritos":
        exibir_logo()
        favoritos_page()
    else:
        exibir_logo()
        st.error("Página não encontrada.")
        st.session_state.page = 'inicio'

if __name__ == "__main__":
    main()

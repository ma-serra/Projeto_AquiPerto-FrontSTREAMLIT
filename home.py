import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Configuração da página
st.set_page_config(page_title="Home", page_icon="🏠", layout="wide")

# Função para codificar a imagem em base64 para exibição no HTML
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Função para centralizar a logo usando HTML e CSS com margens ajustáveis
def display_centered_logo(image_path, width=200, top_margin="-200px", bottom_margin="-200px"):
    if os.path.exists(image_path):
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 60vh; margin-top: {top_margin}; margin-bottom: {bottom_margin};">
                <img src="data:image/png;base64,{encode_image(image_path)}" width="{width}">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Logo não encontrada.")


def botoes_sidebar():
    # Estilização CSS para os botões e títulos das seções
    st.sidebar.markdown("""
    <style>
    /* Estilo para os títulos das seções */
    .section-title {
        font-size: 18px;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #333333;
        font-weight: bold;
    }
    
    /* Estilo para os botões da sidebar */
    a.sidebar-button {
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
    }
    
    a.sidebar-button span {
        position: relative;
        z-index: 2;
    }
    
    a.sidebar-button:after {
        position: absolute;
        content: "";
        top: 0;
        left: 0;
        width: 0;
        height: 100%;
        background: #333;
        transition: all 0.35s;
        border-radius: 5px;
    }
    
    a.sidebar-button:hover {
        color: #fff;
    }
    
    a.sidebar-button:hover:after {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Primeira seção: Acesso (Login e Cadastro)
    st.sidebar.markdown("<div class='section-title'>Acesso</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/login' class='sidebar-button'><span>Login</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/cadastro' class='sidebar-button'><span>Cadastro</span></a>", unsafe_allow_html=True)
    
    # Segunda seção: Navegação (Home, Serviços, Favoritos, Mapa)
    st.sidebar.markdown("<div class='section-title'>Navegação</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/servicos' class='sidebar-button'><span>Serviços</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/favoritos' class='sidebar-button'><span>Favoritos</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/mapa' class='sidebar-button'><span>Mapa</span></a>", unsafe_allow_html=True)

botoes_sidebar()

# Centralizar a logo na área principal
logo_path = 'img/logo_aqui_perto.png'
display_centered_logo(logo_path, width=200)

# Carregar e exibir o conteúdo da página Home
try:
    with open("templates/home.html", "r", encoding="utf-8") as file:
        html_code = file.read()
    components.html(html_code, width=None, height=920, scrolling=False)
except FileNotFoundError:
    st.error("O arquivo 'home.html' não foi encontrado na pasta 'templates'.")

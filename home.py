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

# Função para centralizar a logo usando HTML e CSS
def display_centered_logo(image_path, width=200):
    if os.path.exists(image_path):
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 60vh;">
                <img src="data:image/png;base64,{encode_image(image_path)}" width="{width}">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("Logo não encontrada.")

# Sidebar com botões de Login/Cadastro ou Sair
with st.sidebar:
    st.markdown("# Navegação")
    st.markdown("---")  # Linha separadora

    # Verificar se o usuário está logado
    if st.session_state.get('logged_in'):
        st.write(f"### Bem-vindo, {st.session_state.get('user_email', '')}!")
        if st.button("Sair"):
            st.session_state.clear()
            st.success("Você saiu com sucesso.")
            st.set_query_params()  # Limpar parâmetros da URL
            st.experimental_rerun()
    else:
        st.write("### Acesse sua conta")
        if st.button('Login'):
            st.set_query_params(page='login')
            st.experimental_rerun()
        if st.button('Cadastro'):
            st.set_query_params(page='cadastro')
            st.experimental_rerun()

# Centralizar a logo na área principal
logo_path = 'img/logo_aqui_perto.png'
display_centered_logo(logo_path, width=200)

# Carregar e exibir o conteúdo da página Home
try:
    with open("templates/home.html", "r", encoding="utf-8") as file:
        html_code = file.read()
    components.html(html_code, width=None, height=1025, scrolling=False)
except FileNotFoundError:
    st.error("O arquivo 'home.html' não foi encontrado na pasta 'templates'.")

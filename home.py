import streamlit as st
import requests

api_url = "http://127.0.0.1:5000/home"

# Código da home page aqui

def carregar_conteudo_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao conectar com a API: {e}")
        return {}

# Carrega o conteúdo da API
conteudo = carregar_conteudo_api(api_url)

# Título da página
st.title("Bem-vindo à Nossa Plataforma")

# Exibe uma mensagem da API ou um texto padrão
if conteudo:
    st.write(conteudo.get('message', 'Página inicial'))
else:
    st.write("Bem-vindo! Use os botões abaixo para navegar.")

# Espaçamento
st.markdown("<br>", unsafe_allow_html=True)

# Botão para a próxima página (Mapa)
st.markdown(
    """
    <a href="/mapa" target="_self">
        <button style="display:block; width:200px; height:50px; margin:10px auto; background-color:#004aad; color:white; border:none; border-radius:5px; font-size:16px;">
            Ir para o Mapa
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Botão para Cadastro
st.markdown(
    """
    <a href="/cadastro" target="_self">
        <button style="display:block; width:200px; height:50px; margin:10px auto; background-color:#28a745; color:white; border:none; border-radius:5px; font-size:16px;">
            Cadastro
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

# Botão para Login
st.markdown(
    """
    <a href="/login" target="_self">
        <button style="display:block; width:200px; height:50px; margin:10px auto; background-color:#ffc107; color:white; border:none; border-radius:5px; font-size:16px;">
            Login
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

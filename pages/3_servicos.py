# Instalar a biblioteca streamlit-option-menu
# !pip install streamlit-option-menu

import streamlit as st
from streamlit_option_menu import option_menu
import requests

# URL da API
api_url = "http://127.0.0.1:5000/locais"
response = requests.get(api_url)
locais = response.json()

# Separar os locais por tipo
supermercados = [dicio for dicio in locais["locais"] if dicio["tipo"] == "Supermercado"]
farmacias = [dicio for dicio in locais["locais"] if dicio["tipo"] == "Farmácia"]
shopping_centers = [dicio for dicio in locais["locais"] if dicio["tipo"] == "Shopping center"]
estacionamentos = [dicio for dicio in locais["locais"] if dicio["tipo"] == "Estacionamento"]
restaurantes = [dicio for dicio in locais["locais"] if dicio["tipo"] == "Restaurante"]

sidebar_logo = "img/logo_aqui_perto.png"
main_body_logo = "img/casa_logoaquiperto.png"

st.logo(sidebar_logo, icon_image=main_body_logo)
st.sidebar.markdown("Olá!")


# Menu de navegação
with st.sidebar:
    selected = option_menu("Menu", ["Supermercados", "Farmácias", "Shopping center", "Estacionamentos", "Restaurantes"], 
    icons=["cart4", "capsule", "building", "car-front-fill", "cup-hot"], menu_icon="list", default_index=0)

# Página de Supermercados
if selected == "Supermercados":
    st.title("Supermercados Recomendados")
    st.markdown("""
        <h2>Bem-vindo à nossa página de recomendações de supermercados!</h2>
        <p>Aqui você encontrará uma seleção dos melhores supermercados da cidade.</p>
    """, unsafe_allow_html=True)

    for dicio in supermercados:
        st.markdown(f"""
            <h3>{dicio["nome"]}</h3>
            <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
            <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
            <p><strong>Avaliação:</strong> {dicio["avaliacao"]}⭐</p>
            <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
            <hr>
        """, unsafe_allow_html=True)

# Página de Farmácias
elif selected == "Farmácias":
    st.title("Farmácias Recomendadas")
    st.markdown("""
        <h2>Bem-vindo à nossa página de recomendações de farmácias!</h2>
        <p>Aqui você encontrará uma seleção das melhores farmácias da cidade.</p>
    """, unsafe_allow_html=True)

    for dicio in farmacias:
        st.markdown(f"""
            <h3>{dicio["nome"]}</h3>
            <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
            <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
            <p><strong>Avaliação:</strong> {dicio["avaliacao"]}⭐</p>
            <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
            <hr>
        """, unsafe_allow_html=True)

# Página de Shopping Centers
elif selected == "Shopping center":
    st.title("Shopping Centers Recomendados")
    st.markdown("""
        <h2>Bem-vindo à nossa página de recomendações de shopping centers!</h2>
        <p>Aqui você encontrará uma seleção dos melhores shopping centers da cidade.</p>
    """, unsafe_allow_html=True)

    for dicio in shopping_centers:
        st.markdown(f"""
            <h3>{dicio["nome"]}</h3>
            <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
            <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
            <p><strong>Avaliação:</strong> {dicio["avaliacao"]}⭐</p>
            <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
            <hr>
        """, unsafe_allow_html=True)

# Página de Estacionamentos
elif selected == "Estacionamentos":
    st.title("Estacionamentos Recomendados")
    st.markdown("""
        <h2>Bem-vindo à nossa página de recomendações de estacionamentos!</h2>
        <p>Aqui você encontrará uma seleção dos melhores estacionamentos da cidade.</p>
    """, unsafe_allow_html=True)

    for dicio in estacionamentos:
        st.markdown(f"""
            <h3>{dicio["nome"]}</h3>
            <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
            <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
            <p><strong>Avaliação:</strong> {dicio["avaliacao"]}⭐</p>
            <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
            <hr>
        """, unsafe_allow_html=True)

# Página de Restaurantes
elif selected == "Restaurantes":
    st.title("Restaurantes Recomendados")
    st.markdown("""
        <h2>Bem-vindo à nossa página de recomendações de restaurantes!</h2>
        <p>Aqui você encontrará uma seleção dos melhores restaurantes da cidade.</p>
    """, unsafe_allow_html=True)

    for dicio in restaurantes:
        st.markdown(f"""
            <h3>{dicio["nome"]}</h3>
            <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
            <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
            <p><strong>Avaliação:</strong> {dicio["avaliacao"]}⭐</p>
            <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
            <hr>
        """, unsafe_allow_html=True)


def botoes_sidebar1():
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
        text-decoration: none;
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
    st.sidebar.markdown("<a href='/' class='sidebar-button'><span>Home</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/favoritos' class='sidebar-button'><span>Favoritos</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/mapa' class='sidebar-button'><span>Mapa</span></a>", unsafe_allow_html=True)
    
botoes_sidebar1()

def botoes_sidebar2():
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
    
    /* Estilo para o botão ativo */
    a.sidebar-button.active {
        color: #fff;
    }
    
    a.sidebar-button.active:after {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Obter o valor de 'selected' dos parâmetros da URL
    # query_params = st.experimental_get_query_params()
    # selected = query_params.get('selected', ['Supermercados'])[0]  # Padrão para 'Supermercados' se não definido
    
    # Lista de opções
    options = ["Supermercados", "Farmácias", "Shopping center", "Estacionamentos", "Restaurantes"]
    
    # Ícones correspondentes (opcional: ajuste conforme necessário)
    # icons = {
    #     "Supermercados": "🛒",
    #     "Farmácias": "💊",
    #     "Shopping center": "🏬",
    #     "Estacionamentos": "🚗",
    #     "Restaurantes": "🍽️"
    # }
    
    # Criar botões
    # st.sidebar.markdown("<div class='section-title'>Categorias</div>", unsafe_allow_html=True)
    # for option in options:
    #     active_class = 'active' if selected == option else ''
    #     # URL encode para evitar problemas com espaços
    #     option_encoded = option.replace(" ", "%20")
    #     st.sidebar.markdown(
    #         f"<a href='?selected={option_encoded}' class='sidebar-button {active_class}'><span>{icons.get(option, '')} {option}</span></a>",
    #         unsafe_allow_html=True
    #     )
    
    return selected

botoes_sidebar2()
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
            <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
            <hr>
        """, unsafe_allow_html=True)
import streamlit as st
import requests
# import folium
# from streamlit_folium import st_folium
import streamlit.components.v1 as components

# URL do backend Flask
api_url = "http://127.0.0.1:5000/login"

# Solicita os dados da API
response = requests.get(api_url)
# markers = response.json()  # Recebe os dados em formato JSON

# Renderiza uma seção de cabeçalho personalizada usando HTML e CSS
with open("templates/login.html", "r", encoding="utf-8") as file:
    html_code = file.read()

components.html(html_code, height=500)


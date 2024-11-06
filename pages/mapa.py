import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components
from folium.plugins import LocateControl, MeasureControl
from utils import initialize_session

def mapa_page():
    # Initialize session state
    initialize_session()
    
    # Verify if the user is logged in
    if st.session_state.user_email is None:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state.page = 'login'
        st.rerun()
        return

    api_url = "http://127.0.0.1:5000/locais"

    response = requests.get(api_url)
    markers_data = response.json()

    m = folium.Map(location=[-23.5986884,-46.6765147], zoom_start=15)

    if 'locais' in markers_data:
        markers = markers_data['locais']
    else:
        markers = []
        st.error("Erro: A resposta da API não contém dados de locais.")

    for marker in markers:
        folium.Marker(
            [marker['latitude'], marker['longitude']],
            popup=marker["tipo"],
            tooltip=marker["nome"]
        ).add_to(m)

    LocateControl(auto_start=True).add_to(m)
    m.add_child(MeasureControl())

    # Renderiza uma seção de cabeçalho personalizada usando HTML e CSS
    try:
        with open("templates/map.html", "r", encoding="utf-8") as file:
            html_code = file.read()
        components.html(html_code, height=120)
    except FileNotFoundError:
        st.error("O arquivo 'map.html' não foi encontrado na pasta 'templates'.")

    # Exibe o mapa no Streamlit
    st.write("Mapa Interativo")
    st_folium(m, width=700, height=500)

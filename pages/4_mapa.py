import streamlit as st
import requests
import folium
from streamlit_folium import st_folium
import streamlit.components.v1 as components
from folium.plugins import LocateControl, MeasureControl, BeautifyIcon

api_url = "http://127.0.0.1:5000/locais"

st.set_page_config(initial_sidebar_state="collapsed")

response = requests.get(api_url)
markers_data = response.json()

m = folium.Map(location=[-23.5986884,-46.6765147], zoom_start=15)

if 'locais' in markers_data:
    markers = markers_data['locais']
else:
    markers = []
    st.error("Erro: A resposta da API não contém dados de locais.")

# restaurant_icon = BeautifyIcon(icon="utensils")
# check_icon = BeautifyIcon(icon="check")

for marker in markers:
    # if marker['tipo'] == "restaurante":
    #     marker_icon = restaurant_icon
    # else:
    #     marker_icon = check_icon
    folium.Marker(
        [marker['latitude'], marker['longitude']],
        popup=marker["tipo"],
        # icon= restaurant_icon,
        tooltip=marker["nome"]
    ).add_to(m)

LocateControl(auto_start=True).add_to(m)

m.add_child(MeasureControl())

# Renderiza uma seção de cabeçalho personalizada usando HTML e CSS
with open("templates/map.html", "r", encoding="utf-8") as file:
    html_code = file.read()

components.html(html_code, height=120)

# Exibe o mapa no Streamlit
st.write("Mapa Interativo")
st_folium(m, width=700, height=500)
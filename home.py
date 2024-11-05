import streamlit as st
import requests
import streamlit.components.v1 as components

api_url = "http://127.0.0.1:5000/home"

# Código da home page aqui


with open("templates/home.html", "r", encoding="utf-8") as file:
    html_code = file.read()

components.html(html_code, height=1500)


# st.markdown(
#     """
#     <a href="/mapa" target="_self">
#         <button style="display:block; width:200px; height:50px;">
#             Ir para a próxima página
#         </button>
#     </a>
#     """,
#     unsafe_allow_html=True
# )
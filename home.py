import streamlit as st
import requests
import streamlit.components.v1 as components

with open("templates/home.html", "r", encoding="utf-8") as file:
    html_code = file.read()

st.logo('img\logo_aqui_perto.png', size="large", link=None, icon_image=None)

components.html(html_code, width=None, height=1025, scrolling=False)

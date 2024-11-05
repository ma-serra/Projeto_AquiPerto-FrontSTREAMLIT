import streamlit as st
import requests
import streamlit.components.v1 as components

with open("templates/home.html", "r", encoding="utf-8") as file:
    html_code = file.read()

st.logo('img/logo_aqui_perto.png', size="large", link=None, icon_image=None)

components.html(html_code, width=None, height=1025, scrolling=False)

if st.button('Entrar'):
    st.switch_page('pages/1_login.py')

if st.button('Cadastrar'):
    st.switch_page('pages/2_cadastro.py')

# st.sidebar.success(f"Logado como: {st.session_state['user_email']}")
# if st.button("Sair"):
#     st.session_state.clear()
#     st.experimental_rerun()
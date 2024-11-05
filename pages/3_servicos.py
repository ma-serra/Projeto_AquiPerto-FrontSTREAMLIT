import streamlit as st
import requests

api_url = "http://127.0.0.1:5000/locais"
response = requests.get(api_url)
locais = response.json()

restaurante = locais["locais"]

# Título da página
st.title("Restaurantes Recomendados")

# Descrição
st.markdown("""
	<h2>Bem-vindo à nossa página de recomendações de restaurantes!</h2>
	<p>Aqui você encontrará uma seleção dos melhores restaurantes da cidade.</p>
""", unsafe_allow_html=True)


for dicio in restaurante:
    if dicio["tipo"] == "Restaurante":
        st.markdown(f"""
            <h3>{dicio["nome"]}</h3>
            <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
            <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
            <hr>
        """, unsafe_allow_html=True)


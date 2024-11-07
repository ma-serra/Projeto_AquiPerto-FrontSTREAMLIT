import streamlit as st
import requests
from utils import initialize_session

def cadastrar_local_page():
    initialize_session()
    if st.session_state.user_email is None:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state.page = 'login'
        st.rerun()
        return

    st.title("Cadastrar Novo Local")

    # Formulário para cadastro de novo local
    with st.form("cadastrar_local_form"):
        tipo = st.selectbox("Tipo", ["Supermercado", "Farmácia", "Shopping center", "Estacionamento", "Restaurante"])
        nome = st.text_input("Nome")
        telefone = st.text_input("Telefone")
        endereco = st.text_input("Endereço")
        avaliacao = st.slider("Avaliação", 0.0, 5.0, 0.0, 0.5)
        latitude = st.text_input("Latitude", "-23.595878")
        longitude = st.text_input("Longitude", "-46.686367")
        imagem = st.text_input("URL da Imagem", "https://via.placeholder.com/800x600.png")
        
        submit = st.form_submit_button("Cadastrar")

    if submit:
        if not all([tipo, nome, telefone, endereco, latitude, longitude, imagem]):
            st.warning("Por favor, preencha todos os campos.")
        else:
            try:
                latitude_float = float(latitude)
                longitude_float = float(longitude)
            except ValueError:
                st.error("Latitude e Longitude devem ser números válidos.")
                st.stop()

            data = {
                "tipo": tipo,
                "nome": nome,
                "telefone": telefone,
                "endereco": endereco,
                "avaliacao": str(avaliacao),
                "latitude": latitude_float,
                "longitude": longitude_float,
                "imagem": imagem
            }

            try:
                response = requests.post("http://localhost:5000/locais", json=data)
                if response.status_code == 201:
                    st.success("Local cadastrado com sucesso!")
                    st.session_state.page = 'servicos'
                    st.rerun()
                else:
                    error_message = response.json().get('erro', 'Erro desconhecido.')
                    st.error(f"Erro ao cadastrar local: {error_message}")
            except Exception as e:
                st.error(f"Erro ao conectar com o servidor: {e}")

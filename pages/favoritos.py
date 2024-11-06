import streamlit as st
from utils import initialize_session
import requests

def favoritos_page():

    initialize_session()
    
    if st.session_state.user_email is None:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state.page = 'login'
        st.rerun()
        return

    def carregar_favoritos():
        api_url = f"http://127.0.0.1:5000/favoritos/{st.session_state.user_email}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json().get("favoritos", [])
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao carregar favoritos: {e}")
            return []

    def remover_favorito(id_local):
        api_url = f"http://127.0.0.1:5000/favoritos/{st.session_state.user_email}/remover"
        payload = {"id_local": id_local}
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            st.success("Local removido dos favoritos!")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao remover favorito: {e}")

    st.title("Seus Favoritos")
    st.markdown("""
        <h2>Aqui estão os locais que você adicionou aos seus favoritos:</h2>
    """, unsafe_allow_html=True)
    
    favoritos = carregar_favoritos()
    
    if favoritos:
        for dicio in favoritos:
            avaliacao_formatada = dicio.get("avaliacao", "N/A")
            st.markdown(f"""
                <h3>{dicio["nome"]}</h3>
                <p><strong>Tipo:</strong> {dicio["tipo"]}</p>
                <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
                <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
                <p><strong>Avaliação:</strong> {avaliacao_formatada}⭐</p>
                <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
            """, unsafe_allow_html=True)
            
            if st.button("Remover dos Favoritos", key=f"remover_{dicio['id']}"):
                remover_favorito(dicio['id'])
                st.rerun()
            st.markdown("<hr>", unsafe_allow_html=True)
    else:
        st.info("Você ainda não possui locais favoritos.")

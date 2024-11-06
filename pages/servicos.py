# pages/servicos.py

import streamlit as st
from utils import initialize_session
import requests
from streamlit_option_menu import option_menu

def servicos_page():
    # Inicialização do estado de sessão
    initialize_session()
    
    # Verificar se o usuário está logado
    if st.session_state.user_email is None:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state.page = 'login'
        st.rerun()
        return
    
    # Função para carregar os dados dos locais
    def carregar_dados():
        api_url = "http://127.0.0.1:5000/locais"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao conectar com a API: {e}")
            return None

    # Carregar os dados dos locais
    locais = carregar_dados()
    if locais is None:
        return  # Interrompe a execução se não for possível carregar os dados

    # Separar os locais por tipo
    tipos = ["Supermercado", "Farmácia", "Shopping center", "Estacionamento", "Restaurante"]
    locais_por_tipo = {tipo: [dicio for dicio in locais["locais"] if dicio["tipo"] == tipo] for tipo in tipos}
    
    # Menu de navegação dentro da página de serviços
    selected = option_menu(
        menu_title=None,
        options=["Supermercados", "Farmácias", "Shopping centers", "Estacionamentos", "Restaurantes"],
        icons=["cart4", "capsule", "building", "car-front-fill", "cup-hot"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )
    
    # Mapeamento entre o texto do menu e o tipo usado nos dados
    tipo_map = {
        "Supermercados": "Supermercado",
        "Farmácias": "Farmácia",
        "Shopping centers": "Shopping center",
        "Estacionamentos": "Estacionamento",
        "Restaurantes": "Restaurante"
    }
    
    tipo_selected = tipo_map[selected]
    
    # Exibir os locais correspondentes ao tipo selecionado
    st.title(f"{selected} Recomendados")
    st.markdown(f"""
        <h2>Bem-vindo à nossa página de recomendações de {selected.lower()}!</h2>
        <p>Aqui você encontrará uma seleção dos melhores {selected.lower()} da cidade.</p>
    """, unsafe_allow_html=True)
    
    locais_selecionados = locais_por_tipo.get(tipo_selected, [])
    
    if locais_selecionados:
        for dicio in locais_selecionados:
            st.markdown(f"""
                <h3>{dicio["nome"]}</h3>
                <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
                <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
                <p><strong>Avaliação:</strong> {dicio["avaliacao"]}⭐</p>
                <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
                <hr>
            """, unsafe_allow_html=True)
    else:
        st.write(f"Não há {selected.lower()} disponíveis no momento.")

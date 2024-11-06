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

    # Função para carregar os favoritos do usuário
    def carregar_favoritos():
        api_url = f"http://127.0.0.1:5000/favoritos/{st.session_state.user_email}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            favoritos_ids = [fav['id'] for fav in data.get('favoritos', [])]
            return favoritos_ids
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao carregar favoritos: {e}")
            return []

    # Função para adicionar um local aos favoritos
    def adicionar_favorito(id_local):
        api_url = f"http://127.0.0.1:5000/favoritos/{st.session_state.user_email}/adicionar"
        payload = {"id_local": id_local}
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            st.success("Local adicionado aos favoritos!")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao adicionar favorito: {e}")

    # Função para remover um local dos favoritos
    def remover_favorito(id_local):
        api_url = f"http://127.0.0.1:5000/favoritos/{st.session_state.user_email}/remover"
        payload = {"id_local": id_local}
        try:
            response = requests.post(api_url, json=payload)
            response.raise_for_status()
            st.success("Local removido dos favoritos!")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao remover favorito: {e}")

    # Carregar os dados dos locais
    locais = carregar_dados()
    if locais is None:
        return

    # Carregar os favoritos do usuário
    favoritos_ids = carregar_favoritos()

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
    
    # Selecionar a avaliação mínima desejada
    st.sidebar.markdown("### Filtrar por Avaliação")
    min_avaliacao = st.sidebar.slider("Avaliação mínima", 0.0, 5.0, 0.0, 0.5)
    
    # Função para converter avaliação em float de forma segura
    def safe_float(value, default=0.0):
        try:
            value = str(value).replace(',', '.')  # Substitui vírgula por ponto
            return float(value)
        except (ValueError, TypeError):
            return default
    
    # Adicionar estilização em CSS para os botões
    st.markdown("""
        <style>
        .favorito-button > button {
            width: 100% !important;
            height: 50px !important;
            font-size: 18px !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Exibir os locais correspondentes ao tipo selecionado
    st.title(f"{selected} Recomendados")
    st.markdown(f"""
        <h2>Bem-vindo à nossa página de recomendações de {selected.lower()}!</h2>
        <p>Aqui você encontrará uma seleção dos melhores {selected.lower()} da cidade.</p>
    """, unsafe_allow_html=True)
    
    locais_selecionados = locais_por_tipo.get(tipo_selected, [])
    
    # Filtrar os locais pela avaliação mínima
    locais_filtrados = [dicio for dicio in locais_selecionados if safe_float(dicio.get("avaliacao", 0)) >= min_avaliacao]
    
    if locais_filtrados:
        for dicio in locais_filtrados:
            avaliacao_formatada = safe_float(dicio.get("avaliacao", 0))
            st.markdown(f"""
                <h3>{dicio["nome"]}</h3>
                <p><strong>Endereço:</strong> {dicio["endereco"]}</p>
                <p><strong>Telefone:</strong> {dicio["telefone"]}</p>
                <p><strong>Avaliação:</strong> {avaliacao_formatada}⭐</p>
                <img src="{dicio["imagem"]}" style="width: 100%; border-radius: 10px;">
                <p></p>
            """, unsafe_allow_html=True)
            
            # Determinar o rótulo do botão e a estrela
            if dicio['id'] in favoritos_ids:
                button_label = "⭐ Remover dos Favoritos"
                button_key = f"remover_{dicio['id']}"
                # Classe CSS para o botão
                button_class = 'favorito-button'
                if st.button(button_label, key=button_key):
                    remover_favorito(dicio['id'])
                    st.rerun()
            else:
                button_label = "Adicionar aos Favoritos"
                button_key = f"adicionar_{dicio['id']}"
                # Classe CSS para o botão
                button_class = 'favorito-button'
                if st.button(button_label, key=button_key):
                    adicionar_favorito(dicio['id'])
                    st.rerun()
            
            st.markdown("<hr>", unsafe_allow_html=True)
    else:
        st.write(f"Não há {selected.lower()} com avaliação igual ou superior a {min_avaliacao} no momento.")

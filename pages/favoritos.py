import streamlit as st
from utils import initialize_session

def favoritos_page():
    # Initialize session state
    initialize_session()

    # Verify if the user is logged in
    if st.session_state.user_email is None:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state.page = 'login'
        st.rerun()
        return

    # Initialize the favorites list in the session
    if "favoritos" not in st.session_state:
        st.session_state["favoritos"] = []

    # Function to add or remove a location from favorites
    def toggle_favorito(local):
        if local in st.session_state["favoritos"]:
            st.session_state["favoritos"].remove(local)
            st.success(f"{local} foi removido dos favoritos!")
        else:
            st.session_state["favoritos"].append(local)
            st.success(f"{local} foi adicionado aos favoritos!")

    # Estilização em CSS
    st.markdown(
        """
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: Arial, sans-serif;
                background-color: #FFF3D5;
            }
            header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px;
                background-color: #FFF3D5;
                gap: 20px;
            }
            .logo {
                margin-left: 20px;
            }
            nav a {
                margin: 0 15px;
                text-decoration: none;
                color: black;
                font-weight: bold;
                font-size: 18px;
                display: inline-flex;
                align-items: center;
            }
            nav a img {
                width: 16px;
                height: auto;
                vertical-align: middle;
            }
            .intro {
                text-align: center;
                padding: 40px 20px;
            }
            .intro h1 {
                font-size: 48px;
                margin-bottom: 10px;
            }
            .populares h2 {
                font-size: 32px;
                margin-bottom: 20px;
            }
            .cards {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                gap: 20px;
            }
            .card {
                display: flex;
                flex-direction: column;
                align-items: center;
                text-decoration: none;
                color: black;
                border: 1px solid #ccc;
                padding: 10px;
                border-radius: 8px;
                width: 250px;
                background-color: white;
            }
            .card img {
                width: 250px;
                height: 175px;
                object-fit: cover;
                border-radius: 8px;
            }
            .card span {
                margin-top: 10px;
                font-size: 20px;
                font-weight: bold;
            }
            .estrela {
                font-size: 20px;
                color: gold;
                cursor: pointer;
                margin-top: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Estrutura da interface com HTML
    st.markdown(
        """
        <header>
            <div class="logo">
                <a href="/"><img src="img/logo.png" alt="logo"></a>
            </div>
        </header>
        <main>
            <section class="intro">
                <h1>Favoritos</h1>
                <p>Gerencie seus locais favoritos!</p>
            </section>
            <section class="populares">
                <h2>Locais Populares</h2>
                <div class="cards">
        """,
        unsafe_allow_html=True
    )

    # Exibir cards dos locais populares
    locais = ["Restaurante A", "Shopping B", "Supermercado C"]
    for local in locais:
        st.markdown(
            f"""
            <div class="card">
                <img src="https://via.placeholder.com/250x175" alt="{local}">
                <span>{local}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        # Determinar o símbolo da estrela (favoritado ou não)
        if local in st.session_state["favoritos"]:
            estrela = f"⭐ Remover {local} dos favoritos"
        else:
            estrela = f"☆ Adicionar {local} aos favoritos"
        
        # Botão para adicionar/remover dos favoritos
        if st.button(estrela, key=f"favorito_{local}"):
            toggle_favorito(local)

    st.markdown(
        """
                </div>
            </section>
        </main>
        """,
        unsafe_allow_html=True
    )

    # Exibir favoritos ao final da página
    if st.button("Ver Favoritos"):
        if st.session_state["favoritos"]:
            st.write("Favoritos:", st.session_state["favoritos"])
        else:
            st.write("Nenhum local adicionado aos favoritos.")

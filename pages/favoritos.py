import streamlit as st

# Lista de favoritos
favoritos = st.session_state.get("favoritos", [])

# Função para adicionar ou remover o local dos favoritos
def toggle_favorito(local):
    if local in favoritos:
        favoritos.remove(local)
        st.session_state["favoritos"] = favoritos
        st.success(f"{local} foi removido dos favoritos!")
    else:
        favoritos.append(local)
        st.session_state["favoritos"] = favoritos
        st.success(f"{local} foi adicionado aos favoritos!")

import streamlit as st

# Lista de favoritos
favoritos = st.session_state.get("favoritos", [])

# Função para adicionar ou remover o local dos favoritos
def favoritar(local):
    if local in favoritos:
        favoritos.remove(local)
        st.session_state["favoritos"] = favoritos
        st.success(f"{local} foi removido dos favoritos!")
    else:
        favoritos.append(local)
        st.session_state["favoritos"] = favoritos
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
        <nav>
            <a href="#">Favoritos</a>
            <a href="#">Recentes</a>
            <a href="#">Configurações</a>
            <a href="#"><img src="https://cdn-icons-png.flaticon.com/512/64/64673.png" alt="Buscar"></a>
        </nav>
    </header>
    <main>
        <section class="intro">
            <h1>Bem-vindo ao Aqui Perto</h1>
            <p>Encontre locais incríveis perto de você!</p>
        </section>
        <section class="populares">
            <h2>Locais Populares</h2>
            <div class="cards">
    """,
    unsafe_allow_html=True
)

# Exibir cards dos locais populares
locais = ["Big Big", "Shopping Vila Olímpia", "Pão de açucar"]
for local in locais:
    with st.container():
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
        if local in favoritos:
            estrela = "⭐ Remover dos favoritos"
        else:
            estrela = "☆ Adicionar aos favoritos"
        
        # Botão para adicionar/remover dos favoritos
        if st.button(estrela, key=local):
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
    if favoritos:
        st.write("Favoritos:", favoritos)
    else:
        st.write("Nenhum local adicionado aos favoritos.")
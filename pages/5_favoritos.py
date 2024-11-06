import streamlit as st

# Inicializar a lista de favoritos na sessão
if "favoritos" not in st.session_state:
    st.session_state["favoritos"] = []

# Função para adicionar ou remover o local dos favoritos
def toggle_favorito(local):
    if local in st.session_state["favoritos"]:
        st.session_state["favoritos"].remove(local)
        st.success(f"{local} foi removido dos favoritos!")
    else:
        st.session_state["favoritos"].append(local)
        st.success(f"{local} foi adicionado aos favoritos!")

def botoes_sidebar():
    # Estilização CSS para os botões e títulos das seções
    st.sidebar.markdown("""
    <style>
    /* Estilo para os títulos das seções */
    .section-title {
        font-size: 18px;
        margin-top: 20px;
        margin-bottom: 10px;
        color: #333333;
        font-weight: bold;
    }
    
    /* Estilo para os botões da sidebar */
    a.sidebar-button {
        display: block;
        width: 100%;
        height: 40px;
        line-height: 40px;
        font-size: 16px;
        font-family: sans-serif;
        text-decoration: none;
        color: #333;
        border: 2px solid #333;
        letter-spacing: 1px;
        text-align: center;
        position: relative;
        transition: all 0.35s;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    
    a.sidebar-button span {
        position: relative;
        z-index: 2;
    }
    
    a.sidebar-button:after {
        position: absolute;
        content: "";
        top: 0;
        left: 0;
        width: 0;
        height: 100%;
        background: #333;
        transition: all 0.35s;
        border-radius: 5px;
    }
    
    a.sidebar-button:hover {
        color: #fff;
    }
    
    a.sidebar-button:hover:after {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Primeira seção: Acesso (Login e Cadastro)
    st.sidebar.markdown("<div class='section-title'>Acesso</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/login' class='sidebar-button'><span>Login</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/cadastro' class='sidebar-button'><span>Cadastro</span></a>", unsafe_allow_html=True)
    
    # Segunda seção: Navegação (Home, Serviços, Favoritos, Mapa)
    st.sidebar.markdown("<div class='section-title'>Navegação</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/' class='sidebar-button'><span>Home</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/servicos' class='sidebar-button'><span>Serviços</span></a>", unsafe_allow_html=True)
    st.sidebar.markdown("<a href='/mapa' class='sidebar-button'><span>Mapa</span></a>", unsafe_allow_html=True)

botoes_sidebar()

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
            width: 16px; /* Tamanho da imagem de lupa ajustado */
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
locais = ["Restaurante A", "Shopping B", "Supermercado C"]
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
        if local in st.session_state["favoritos"]:
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
    if st.session_state["favoritos"]:
        st.write("Favoritos:", st.session_state["favoritos"])
    else:
        st.write("Nenhum local adicionado aos favoritos.")
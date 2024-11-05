import streamlit as st
import requests

# URL do backend Flask (sem o endpoint específico)
API_URL = "http://localhost:5000"

def main():
    st.title("Aplicativo de Cadastro")

    menu = ["Cadastro"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Cadastro":
        st.subheader("Cadastro")

        # Campos do formulário de cadastro
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type='password')
        confirmar_senha = st.text_input("Confirmar Senha", type='password')

        if st.button("Cadastrar"):
            if nome and email and senha and confirmar_senha:
                if senha != confirmar_senha:
                    st.error("As senhas não coincidem.")
                else:
                    data = {
                        'nome': nome,
                        'email': email,
                        'senha': senha
                    }
                    try:
                        # Envia a requisição POST para o endpoint correto
                        response = requests.post(f"{API_URL}/usuarios", json=data)
                        if response.status_code == 201:
                            st.success("Cadastro realizado com sucesso! Por favor, faça login.")
                            # Redirecionar para a página de login ??????????????????????????????????????
                        elif response.status_code == 409:
                            error_message = response.json().get('erro', 'Email já cadastrado.')
                            st.error(f"Erro no cadastro: {error_message}")
                        else:
                            error_message = response.json().get('erro', 'Erro desconhecido.')
                            st.error(f"Erro no cadastro: {error_message}")
                    except Exception as e:
                        st.error(f"Erro ao conectar com o servidor: {e}")
            else:
                st.warning("Por favor, preencha todos os campos.")

    # Área após cadastro ??????????????????????????????????????w

if __name__ == '__main__':
    main()

# URL base do seu backend (substitua pela URL do seu serviço em produção)
base_url = "https://aps-3-flask-rest-mongo-0tomz-1.onrender.com"

# Funções para interação com o backend

# Funções de Usuários
def get_usuarios():
    response = requests.get(f"{base_url}/usuarios")
    return response.json()

def get_usuario_by_id(id_usuario):
    response = requests.get(f"{base_url}/usuarios/{id_usuario}")
    return response.json()

def create_usuario(cpf, nome, data_de_aniversario):
    usuario = {"cpf": cpf, "nome": nome, "data_de_aniversario": data_de_aniversario}
    response = requests.post(f"{base_url}/usuarios", json=usuario)
    return response.json()

def update_usuario(id_usuario, cpf, nome, data_de_aniversario):
    usuario = {"cpf": cpf, "nome": nome, "data_de_aniversario": data_de_aniversario}
    response = requests.put(f"{base_url}/usuarios/{id_usuario}", json=usuario)
    return response.json()

def delete_usuario(id_usuario):
    response = requests.delete(f"{base_url}/usuarios/{id_usuario}")
    return response.json()
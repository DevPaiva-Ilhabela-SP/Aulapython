import requests
from faker import Faker
import json

fake = Faker('pt_BR')

def criar_persona() -> dict:
    """
    Cria dados fictícios para um novo usuário.
    """
    data = {
        "username" : fake.user_name(),
        "email" : fake.email(),
        "password" : fake.password(),
        "phone" : fake.phone_number(),
        "address" : fake.address(),
        "cpf" : fake.cpf()
    }
    return data

def salvar_json(persona_criacao_json: str, conteudo: dict):
    """
    Salva um dicionário como JSON em um arquivo.
    """
    with open(persona_criacao_json, 'w') as arquivo:
        json.dump(conteudo, arquivo)
    print(f'Dados salvos em {persona_criacao_json}.')

def criar_user_api(usuario: dict) -> bool:
    """
    Cria um usuário na API usando dados fornecidos.
    Retorna True se o usuário foi criado com sucesso, False caso contrário.
    """
    endpoint_criaruser = "https://desafiopython.jogajuntoinstituto.org/api/users/"
    response = requests.post(endpoint_criaruser, json=usuario)

    if response.status_code == 201:
        print('Usuário criado com sucesso!')
        print('Status code:', response.status_code)
        print(response.json())
        salvar_json('log_criacao.json', response.json())
        return True
    else:
        print('Falha ao criar usuário.')
        print('Status code: ', response.status_code)
        print('Resposta: ', response.json())
        salvar_json('log_criacao.json', response.json())
        return False

def login_user_api(usuario: dict) -> bool:
    """
    Realiza login na API com os dados do usuário fornecidos.
    """
    endpoint_login = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'
    login_data = {
        'email': usuario["email"],
        'password': usuario["password"]
    }

    response = requests.post(endpoint_login, json=login_data)

    if response.status_code == 200:
        print('Login realizado com sucesso!')
        print('Status code:', response.status_code)
        print(response.json())
        salvar_json('resposta_login.json', response.json())
    else:
        print('Falha ao realizar login.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('resposta_login.json', response.json())

# Criar um novo usuário fictício
usuario = criar_persona()

# Criar o usuário na API
if criar_user_api(usuario):
    # Realizar login com o usuário criado
    login_user_api(usuario)



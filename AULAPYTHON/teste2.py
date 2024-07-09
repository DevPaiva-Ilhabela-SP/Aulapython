from faker import Faker
import requests
import json

Faker = Faker('pt_BR')

def create_persona() -> dict:

    username = Faker.name().replace(' ', '')
    data = {
        'username': username,
        'email': Faker.email(),
        'password': Faker.password(),
        'phone': Faker.phone_number(),
        'address': Faker.address(),
        'cpf': Faker.cpf()
    }
    return data
 
persona = create_persona()

url = 'https://desafiopython.jogajuntoinstituto.org/api/users/'

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(persona))

if response.status_code >= 200 and response.status_code < 299:
    print('Dados enviados com sucesso!')
else:
    print(f'Falha ao enviar dados. Status code: {response.status_code}')

print(persona)

url_2 = 'https://desafiopython.jogajuntoinstituto.org/api/users/login/'

response = requests.post(url_2, json=persona)


login_data = {
    'email': persona["email"],
    'password': persona["password"]
}

print(login_data)

login_response = requests.post(url_2, json=login_data)

if login_response.status_code >= 200 and login_response.status_code < 300:
    print("    ")
    print('Login bem-sucedido!')
    print("    ")
    print(f'Login Response: {login_response.json()}')
    response_json = login_response.json()
    
    nome_arquivo = 'token_de_usuario'
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(response_json, arquivo, indent=4)
else:
    print('A senha ou o email está incorreto, tente novamente.')
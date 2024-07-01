# Estrutura de dicionário com nome e CEP de cada integrante
squad = {
    'Anderson': {
        'cep': '12200-000',
        'cidade': 'São José dos Campos'
    },
    'Allyph': {
        'cep': '11660-000',
        'cidade': 'Caraguatatuba'
    },
    'Felipe': {
        'cep': '11630-000',
        'cidade': 'Ilhabela'
    },
    'Gabriel': {
        'cep': '11600-000',
        'cidade': 'São Sebastião'
    },
    'Rodrigo': {
        'cep': '11680-000',
        'cidade': 'Ubatuba'
    }
}

# Requisição para imprimir nome e cidade de cada integrante
for nome, info in squad.items():
    print(f"Nome: {nome}, Cidade: {info['cidade']}")

# Criação do arquivo requirements.txt
with open('requirements.txt', 'w') as file:
    file.write('requests\n')

print("Arquivo requirements.txt gerado com sucesso!")

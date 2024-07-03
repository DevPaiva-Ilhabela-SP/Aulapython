# Estrutura de dicionário com nome e CEP de cada integrante
# Importando a biblioteca necessária
import requests

# Estrutura de dicionário com nome e cep de cada integrante
squad = {
    'Anderson': '01311-200',
    'Allyph': '04571-010',
    'Gabriel': '12245-670',
    'Luiz Felipe': '70070-150',
    'Rodrigo': '11630-370'
}

# Função para obter a cidade a partir do CEP
def get_city_from_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('localidade')
    else:
        return None

# Gerar arquivo requirements.txt
with open('requirements.txt', 'w') as file:
    file.write('requests\n')

# Imprimir nome e cidade de cada integrante do squad
for nome, cep in squad.items():
    cidade = get_city_from_cep(cep)
    if cidade:
        print(f'Nome: {nome} | Cidade: {cidade}')
    else:
        print(f'Nome: {nome} | Cidade não encontrada para o CEP: {cep}')
print("Arquivo requirements.txt gerado com sucesso!")


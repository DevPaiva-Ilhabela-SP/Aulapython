from faker import Faker
import random
import csv

def criar_persona():
    fake = Faker('pt_BR') 
    nome = fake.name()
    cidade = fake.city()
    idade = random.randint(18, 80)
    return {'nome': nome, 'cidade': cidade, 'idade': idade}

def salvar_csv(persona, nome_arquivo):
    campos = ['nome', 'cidade', 'idade']

    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writeheader()
        for persona in persona:
            escritor.writerow(persona)

def main():
    persona = []
    for _ in range(1): 
        persona.append(criar_persona())

    nome_arquivo = 'persona_faker.csv'
    salvar_csv(persona, nome_arquivo)
    print(f'Dados da persona foram salvos no arquivo "{nome_arquivo}".')

if __name__ == '__main__':
    main()

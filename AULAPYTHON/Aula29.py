import csv

def criar_persona(nome, cidade, idade):
    return {'nome': nome, 'cidade': cidade, 'idade': idade}

def salvar_csv(personas, nome_arquivo):
    campos = ['nome', 'cidade', 'idade']

    
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

    
        escritor.writeheader()

    
        for persona in personas:
            escritor.writerow(persona)

def main():

    personas = [
        criar_persona('Maria', 'São Paulo', 28),
        criar_persona('João', 'Rio de Janeiro', 32),
        criar_persona('Ana', 'Belo Horizonte', 25)
    ]
    nome_arquivo = 'personas.csv'

    salvar_csv(personas, nome_arquivo)
    print(f'Dados das personas foram salvos no arquivo "{nome_arquivo}".')

if __name__ == '__main__':
    main()

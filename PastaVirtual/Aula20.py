import os

# Lista de dados fictícios
dados = [
    {'nome': 'João', 'email': 'joao@gmail.com'},
    {'nome': 'Maria', 'email': 'maria@hotmail.com'},
    {'nome': 'Pedro', 'email': 'pedro@yahoo.com'},
    {'nome': 'Ana', 'email': 'ana@example.com'}
]

# Nome da pasta onde o arquivo será salvo
nome_pasta = 'arquivos_desafio'

# Verifica se a pasta já existe, senão cria ela
if not os.path.exists(nome_pasta):
    os.makedirs(nome_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso!")

# Caminho completo para o arquivo de texto
caminho_arquivo = os.path.join(nome_pasta, 'dados.txt')

# Escreve os dados no arquivo de texto
with open(caminho_arquivo, 'w') as arquivo:
    for dado in dados:
        arquivo.write(f"Nome: {dado['nome']}, Email: {dado['email']}\n")

print(f"Arquivo '{caminho_arquivo}' criado com sucesso!")

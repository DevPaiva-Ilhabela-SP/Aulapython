# Criando a tupla com 5 dados
tupla_dados = (1, 2, 3, 4, 5)

# Convertendo a tupla em lista
lista_dados = list(tupla_dados)

# Inserindo 2 dados extras na lista
lista_dados.append(6)
lista_dados.append(7)

# Removendo o primeiro dado da lista
primeiro_dado = lista_dados.pop(0)

# Removendo o último dado da lista
ultimo_dado = lista_dados.pop()

# Imprimindo o primeiro dado da lista
print(f"Primeiro dado da lista: {primeiro_dado}")

# Imprimindo a quantidade de dados na lista
print(f"Quantidade de dados na lista: {len(lista_dados)}")

# Criando um dicionário com Nome, Idade e Profissão
dados_pessoa = {
    'Nome': 'João',
    'Idade': 30,
    'Profissão': 'Engenheiro'
}

# Imprimindo o valor contido na chave nome,idade e profissão, do dicionário
print(f"Nome: {dados_pessoa['Nome']}")
print(f"Idade: {dados_pessoa['Idade']}")
print(f"Pofissão: {dados_pessoa['Profissão']}")
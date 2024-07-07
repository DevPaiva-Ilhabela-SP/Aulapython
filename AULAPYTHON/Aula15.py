tupla_dados = (1, 2, 3, 4, 5)


lista_dados = list(tupla_dados)


lista_dados.append(6)
lista_dados.append(7)


primeiro_dado = lista_dados.pop(0)

ultimo_dado = lista_dados.pop()


print(f"Primeiro dado da lista: {primeiro_dado}")


print(f"Quantidade de dados na lista: {len(lista_dados)}")


dados_pessoa = {
    'Nome': 'João',
    'Idade': 30,
    'Profissão': 'Engenheiro'
}


print(f"Nome: {dados_pessoa['Nome']}")
print(f"Idade: {dados_pessoa['Idade']}")
print(f"Pofissão: {dados_pessoa['Profissão']}")
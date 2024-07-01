# Criando a lista de frutas
lista_frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']

# Criando a lista de alergias
lista_alergias = ['abacaxi', 'kiwi', 'melancia']

# Inserindo uma fruta da lista de frutas na lista de alergias
fruta_alergica = 'laranja'
lista_alergias.append(fruta_alergica)

# Verificando se cada fruta da lista está na lista de alergias

consultar_fruta =input("Digite a fruta que desja consultar: ")
for lista_frutas in lista_frutas:
    print("frutas não alergicas")
    if lista_alergias in lista_alergias:
        print("frutas alergicas")

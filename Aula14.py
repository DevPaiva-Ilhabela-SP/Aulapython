# Lista de frutas
lista_frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']

# Lista de alergias
lista_alergias = ['abacaxi', 'kiwi', 'pêssego']

# Adicionar uma fruta da lista de frutas na lista de alergias
fruta_alergica = lista_frutas[2]  # Vamos escolher a laranja para adicionar às alergias
lista_alergias.append(fruta_alergica)

# Verificar cada fruta na lista de frutas
for fruta in lista_frutas:
    # Verificar se a fruta está na lista de alergias
    if fruta in lista_alergias:
        print(f"{fruta} está na lista de alergias.")
    else:
        print(f"{fruta} não está na lista de alergias.")

lista_frutas = ['maçã', 'banana', 'laranja', 'uva', 'morango']

lista_alergias = ['abacaxi', 'kiwi', 'pêssego']

fruta_alergica = lista_frutas[2]  
lista_alergias.append(fruta_alergica)


for fruta in lista_frutas:
  
    if fruta in lista_alergias:
        print(f"{fruta} está na lista de alergias.")
    else:
        print(f"{fruta} não está na lista de alergias.")

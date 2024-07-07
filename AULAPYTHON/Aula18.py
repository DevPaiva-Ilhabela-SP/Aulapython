def contar_vogais(palavra):

    contador = 0
    
    vogais = 'aeiouAEIOU'  
    
    
    for caractere in palavra:
    
        if caractere in vogais:
            contador += 1
    
    return contador
palavra_usuario = input("Digite uma palavra para contar as vogais: ")

total_vogais = contar_vogais(palavra_usuario)

print(f"A palavra '{palavra_usuario}' tem {total_vogais} vogais.")

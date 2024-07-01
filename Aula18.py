def contar_vogais(palavra):
    # Inicializa o contador de vogais
    contador = 0
    # Define as vogais
    vogais = 'aeiouAEIOU'  # Incluímos tanto minúsculas quanto maiúsculas
    
    # Itera sobre cada caractere na palavra
    for caractere in palavra:
        # Verifica se o caractere é uma vogal
        if caractere in vogais:
            contador += 1
    
    return contador

# Solicitação de entrada do usuário
palavra_usuario = input("Digite uma palavra para contar as vogais: ")

# Chama a função para contar as vogais na palavra inserida
total_vogais = contar_vogais(palavra_usuario)

# Imprime o resultado
print(f"A palavra '{palavra_usuario}' tem {total_vogais} vogais.")

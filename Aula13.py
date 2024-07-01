# Pedindo ao usuário para inserir um número para a tabuada
numero = int(input("Digite um número para ver a sua tabuada: "))

# Imprimindo a tabuada do número inserido
print(f"Tabuada do {numero}:")
for i in range(1, 11):  # i variará de 1 a 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

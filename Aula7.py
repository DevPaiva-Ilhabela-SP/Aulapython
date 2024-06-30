import math

# Solicitar ao usuário um valor
valor = float(input("Digite um valor: "))

# Calcular os outputs conforme especificado
output1 = valor * 2
output2 = valor * 3
output3 = valor ** 2
output4 = math.sqrt(valor)  # Raiz quadrada usando a função math.sqrt
output5 = valor ** (1/3)    # Raiz cúbica é equivalente a valor elevado a (1/3)

# Exibir os resultados
print(f"O dobro de {valor} é: {output1}")
print(f"O triplo de {valor} é: {output2}")
print(f"{valor} ao quadrado é: {output3}")
print(f"A raiz quadrada de {valor} é: {output4}")
print(f"A raiz cúbica de {valor} é: {output5}")

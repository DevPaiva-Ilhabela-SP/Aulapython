# Capturando os dados do usuário
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
idade = int(input("Digite sua idade: "))

# Imprimindo os dados na tela
print("\nDados do usuário:")
print(f"Nome: {nome}")
print(f"Altura: {altura} metros")
print(f"Idade: {idade} anos")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calculando a soma das notas
soma_notas = nota1 + nota2

# Imprimindo os dados na tela
print("\nDados do usuário:")
print(f"Nome: {nome}")
print(f"Altura: {altura} metros")
print(f"Idade: {idade} anos")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Soma das notas: {soma_notas}")
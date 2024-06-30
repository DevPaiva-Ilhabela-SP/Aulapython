# Solicitar ao usuário as 4 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcular a média aritmética das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibir a mensagem formatada com o nome do aluno e sua média
nome_aluno = "Caique"  # Aqui você pode substituir pelo nome do aluno desejado
print(f"Olá, {nome_aluno}! Sua média é: {media:.2f} pontos")

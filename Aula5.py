# Definir os valores por banho e custos por porte de cachorro
valores_por_banho = {
    "grande": {"banho": 75.00, "custo": 20.00},
    "médio": {"banho": 60.00, "custo": 15.00},
    "pequeno": {"banho": 50.00, "custo": 5.00}
}

# Exemplo de cálculo para um cachorro específico
nome_pet = "Tuco"
idade_pet = 5  # Suponhamos que Tuco tenha 5 anos de cachorro
porte_pet = "grande"  # Suponhamos que Tuco seja de grande porte
numero_banhos = 10  # Suponhamos que Tuco tome 10 banhos em 12 meses

# Calcular o lucro por banho
lucro_por_banho = valores_por_banho[porte_pet]["banho"] - valores_por_banho[porte_pet]["custo"]

# Calcular o lucro total em 12 meses
lucro_total = lucro_por_banho * numero_banhos

# Exibir a informação ao usuário
print(f"Olá, {nome_pet} tem {idade_pet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}")

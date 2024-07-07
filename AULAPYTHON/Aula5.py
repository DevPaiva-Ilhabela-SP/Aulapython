valores_por_banho = {
    "grande": {"banho": 75.00, "custo": 20.00},
    "médio": {"banho": 60.00, "custo": 15.00},
    "pequeno": {"banho": 50.00, "custo": 5.00}
}


nome_pet = "Tuco"
idade_pet = 5  
porte_pet = "grande" 
numero_banhos = 10 


lucro_por_banho = valores_por_banho[porte_pet]["banho"] - valores_por_banho[porte_pet]["custo"]

lucro_total = lucro_por_banho * numero_banhos


print(f"Olá, {nome_pet} tem {idade_pet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro_total:.2f}")

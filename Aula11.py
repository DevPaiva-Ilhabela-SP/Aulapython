# Solicita o valor total da compra ao usuário
valor_total = float(input("Digite o valor total da sua compra: R$ "))

# Verifica se o cliente qualifica para o vale-compras
if valor_total >= 100.00:
    print("SUA SAÚDE É O QUE IMPORTA. APRESENTE ESSE CUPOM EM SUA PRÓXIMA COMPRA E GANHE R$10 REAIS DE DESCONTO.")
else:
    print("OBRIGADO POR ESCOLHER A MINHA FARMA. VOCÊ SABIA QUE COMPRAS ACIMA DE R$100 REAIS GERAM UM VOUCHER DE R$10 REAIS DE DESCONTO PARA A PRÓXIMA COMPRA?")

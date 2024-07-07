def verificar_paridade(numero):
    if numero % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")



numero_matricula=int(input("Digite o numero de matricula:"))
verificar_paridade(numero_matricula)
def verifica_frete_gratis(cep):

    estados_norte_nordeste = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'MA', 'PA', 'PB', 'PE', 'PI', 'RN', 'RO', 'RR', 'SE', 'TO']

    
    cep = cep.replace('-', '')


    estado_cep = cep[:2]

    
    if estado_cep in estados_norte_nordeste:
        return "Frete GRÁTIS para sua região!"
    else:
        return "Frete não grátis para sua região."

cep_usuario = input("Digite seu CEP: ")
resultado = verifica_frete_gratis(cep_usuario)
print(resultado)
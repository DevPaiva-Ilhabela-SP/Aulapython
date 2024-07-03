def verifica_frete_gratis(cep):
    # Lista de estados das regiões Norte e Nordeste
    estados_norte_nordeste = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'MA', 'PA', 'PB', 'PE', 'PI', 'RN', 'RO', 'RR', 'SE', 'TO']

    # Remover hífen do CEP, se existir
    cep = cep.replace('-', '')

    # Extrair os dois primeiros dígitos do CEP para identificar o estado
    estado_cep = cep[:2]

    # Verificar se o estado está na lista de estados do Norte/Nordeste
    if estado_cep in estados_norte_nordeste:
        return "Frete GRÁTIS para sua região!"
    else:
        return "Frete não grátis para sua região."

# Exemplo de uso
cep_usuario = input("Digite seu CEP: ")
resultado = verifica_frete_gratis(cep_usuario)
print(resultado)
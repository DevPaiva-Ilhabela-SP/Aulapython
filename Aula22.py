print('Digite seu CEP no formato (xxxxx-xxx)')

# Intervalos de CEPs do Norte
ceps_do_norte = [
     '69000-000', '69299-999', # Amazonas
     '69300-000', '69389-999', # Roraima
     '68900-000', '68929-999', # Amapá
     '66000-000', '68899-999', # Pará
     '76800-000', '76999-999', # Rondônia
     '77000-000', '77995-999', # Tocantins
     '69900-000', '69929-999'  # Acre
]

# Intervalos de CEPs do Nordeste
ceps_do_nordeste = [
     '65000-000', '65999-999', # Maranhão
     '64000-000', '64999-999', # Piauí
     '40000-000', '48999-999', # Bahia
     '60000-000', '63999-999', # Ceará
     '59000-000', '59999-999', # Rio Grande do Norte
     '58000-000', '58999-999', # Paraíba
     '50000-000', '56999-999', # Pernambuco
     '57000-000', '57999-999', # Alagoas
     '49000-000', '49999-999'  # Sergipe
]

def cep_to_int(cep):
    return int(cep.replace('-', ''))

def esta_no_intervalo(intervalos):
    for inicio, fim in intervalos:
        if cep_to_int >= cep_to_int(inicio) and cep_to_int <= cep_to_int(fim):
            return True
    return False

def seu_cep(cep):
    if   esta_no_intervalo(ceps_do_norte):
        print('A região Norte tem frete grátis')
    elif esta_no_intervalo(ceps_do_nordeste):
        print('A região do Nordeste tem frete grátis')
    else:
        print('A sua região não tem frete grátis')

cep = input('Digite seu CEP: ')
seu_cep(cep)
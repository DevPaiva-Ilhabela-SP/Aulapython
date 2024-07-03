import requests

# Lista de estados das regiões Norte e Nordeste
norte_nordeste = [
    'AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO', # Norte
    'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE' # Nordeste
]

def validar_cep(cep):
    return len(cep) == 8 and cep.isdigit()

def obter_estado_por_cep(cep):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        data = response.json()
        return data.get('uf')
    except Exception as e:
        print(f"Erro ao consultar o CEP: {e}")
        return None

def verificar_frete_gratis(cep):
    if not validar_cep(cep):
        return "CEP inelegível para o frete grátis."

    estado = obter_estado_por_cep(cep)
    if estado in norte_nordeste:
        return "Frete grátis disponível para este CEP."
    else:
        return "Frete grátis não disponível para este CEP."

# Exemplo de uso
cep = input("Digite o CEP: ")
mensagem = verificar_frete_gratis(cep)
print(mensagem)

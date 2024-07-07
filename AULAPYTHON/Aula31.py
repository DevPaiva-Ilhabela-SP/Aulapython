import csv

def carregar_dados_csv(dados_ficticios):
    with open(dados_ficticios, mode='r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        dados = list(leitor)
    return dados

def filtrar_pessoas(dados, idade_minima=None, renda_minima=None):
    pessoas_filtradas = []

    for pessoa in dados:
        idade = int(pessoa['idade'])
        renda = float(pessoa['renda'].replace(',', '.'))

        if idade_minima is not None and idade <= idade_minima:
            continue
        
        if renda_minima is not None and renda <= renda_minima:
            continue
        
        pessoas_filtradas.append(pessoa)
    
    return pessoas_filtradas

def main():
    nome_arquivo = 'dados_ficticios.csv'
    dados = carregar_dados_csv(nome_arquivo)

    pessoas_idade_maior_40 = filtrar_pessoas(dados, idade_minima=40)
    pessoas_renda_maior_5mil = filtrar_pessoas(dados, renda_minima=5000)
    pessoas_renda_maior_15mil = filtrar_pessoas(dados, renda_minima=15000)

    print(f"Pessoas com idade maior que 40 anos: {len(pessoas_idade_maior_40)}")
    print(f"Pessoas com renda maior que 5 mil: {len(pessoas_renda_maior_5mil)}")
    print(f"Pessoas com renda maior que 15 mil: {len(pessoas_renda_maior_15mil)}")

if __name__ == '__main__':
    main()

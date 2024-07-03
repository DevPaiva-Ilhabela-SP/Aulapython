import os
lista_de_frutas = [
    'Maçã',
    'Banana',
    'Laranja',
    'Morango',
    'Uva'
]
nome_pasta = 'Quitanda_da_véia_chica'

try:
    os.makedirs(nome_pasta)  
    print(f'Pasta "{nome_pasta}" criada com sucesso!')
except FileExistsError:
    print(f'A pasta "{nome_pasta}" já existe.')


nome_arquivo = os.path.join(nome_pasta, 'frutas.txt')

try:
    with open(nome_arquivo, 'w') as arquivo:
        for fruta in lista_de_frutas:
            arquivo.write(fruta + '\n')
    print(f'Arquivo "{nome_arquivo}" criado e dados salvos com sucesso!')
except IOError as e:
    print(f'Erro ao tentar salvar o arquivo: {e}')

print('Compra concluída!')


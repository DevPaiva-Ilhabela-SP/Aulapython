def verifica_par_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
matriculas = []
while len(matriculas) < 5:
    try:
        matricula = int(input(f'Insira o número de matrícula {len(matriculas) + 1}: '))
        matriculas.append(matricula)
    except ValueError:
        print('Por favor, insira um número válido.')
for numero in matriculas:
    resultado = verifica_par_impar(numero)
    print(f'O número de matrícula {numero} é {resultado}.')

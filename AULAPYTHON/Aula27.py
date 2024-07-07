import pandas as pd
dados = {
    'Nome': ['carol', 'joana', 'raquel', 'jessica', 'carla', 'andressa', 'kelli'],
    'Idade': [30, 25, 40, 35, 28, 22, 33],
    'Cidade': ['Recife', 'Salvador', 'Recife', 'Manaus', 'Salvador', 'São Paulo', 'Recife']
}

df = pd.DataFrame(dados)
moradores_recife = df[df['Cidade'] == 'Recife']
print("Moradores do Recife:")
print(moradores_recife)
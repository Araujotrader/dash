import pandas as pd
import potly

#dados = pd.read_csv('teste.csv')

dados = pd.read_csv('teste.csv')

print(dados.describe())
print(dados.info())

print(dados.head(10))

print(dados[(dados['continent'] == 'Americas')])




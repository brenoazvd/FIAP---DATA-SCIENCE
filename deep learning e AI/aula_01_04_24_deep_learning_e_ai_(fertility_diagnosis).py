# -*- coding: utf-8 -*-
"""Aula 01_04_24_Deep Learning e AI (fertility_Diagnosis).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/179YzaAwgBOiDwYBPM6VIZFWkHlLNIqqj

## Diagnóstico de Fertilidade com Pré-Processamento de Dados e Classificação k-NN

## Breno Azevedo
"""

import pandas as pd
import numpy as np


df = pd.read_csv("/home/fertility_Diagnosis.txt")
df

df.isna().sum() #verificando se a NaNs

df.shape # (linhas, colunas)

df = pd.get_dummies(df, columns=['doencas_infantis', 'acidente', 'cirurgia', 'febre'])

df = pd.get_dummies(df, columns=['alcool', 'temporada'])

df

from scipy.stats import shapiro
# Verificar normalidade usando o teste de Shapiro-Wilk
def verifica_normalidade(dataframe, coluna):
    coluna_data = dataframe[coluna]
    # Realizar o teste de Shapiro-Wilk
    statistic, p_valor = shapiro(coluna_data)
    # Definir o nível de significância
    nivel_significancia = 0.1
    # Verificar se a hipótese nula de normalidade pode ser rejeitada
    if p_valor > nivel_significancia:
        print(f"A coluna '{coluna}' segue uma distribuição normal")
        return True
    else:
        print(f"A coluna '{coluna}' não segue uma distribuição normal")
        return False

def normalizar(x):
  return (x - np.min(x))/(np.max(x) - np.min(x))

def padronizar(x):
    return (x -np.mean(x))/np.std(x)

# Chamando a função para verificar normalidade
for coluna in ['idade', 'sentado']:
  if verifica_normalidade(df, coluna):
    df[coluna] = padronizar(df[coluna])#se for distribuição normal, padroniza
  else:#senão, normaliza
    df[coluna] = normalizar(df[coluna])

import seaborn as sb
sb.pairplot(df[['idade',  'alcool', 'fumo' ,'sentado', 'temporada', 'classe']], hue='classe')

df.fumo.unique()

df.idade.unique()

df.sentado.unique()

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

y = df['classe']#classe (saída)
X = df.drop('classe', axis=1)#entradas

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#A gente sempre usa as entradas de dados como X máiusculo
# (idica que são mais de uma entra) entradas: todas as outras colunas com exceção 'sobreviveu'

knn = KNeighborsClassifier(n_neighbors=27)

#treinar o modelo kNN
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

#Avaliar a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print('Acurácia do modelo kNN:', accuracy)

#testando o k ideal
for k in range(3,51,2):
  knn = KNeighborsClassifier(n_neighbors=k)
  # Treinar o modelo kNN
  knn.fit(X_train, y_train)
  y_pred = knn.predict(X_test)

  # Avaliar a acurácia do modelo
  accuracy = accuracy_score(y_test, y_pred)
  print(f'Acurácia para k={k}:', accuracy)
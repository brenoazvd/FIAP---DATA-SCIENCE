# -*- coding: utf-8 -*-
"""GS_DEEP_LEARNING_AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r-UvEdxm3keid1Th4Wq3TvZkQut5YYIg

**Global Solutions 2TSC – 1º semestre de 2024
Deep Learning & AI
Professor Hellynson**

# Classificação de Espécies Marinhas com Deep Learning e Algoritmos de Machine Learning

BRENO RODRIGUES AZEVEDO

##Bibliotecas
"""

import pandas as pd
import numpy as np
import seaborn as sb
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

"""##a)PRÉ-PROCESSAMENTO DE *DADOS*"""

df = pd.read_csv("/home/gs_dataframe.csv", encoding = "cp1252")

def normalizar(x):
  return (x - np.min(x))/(np.max(x) - np.min(x))

def padronizar(x):
    return (x -np.mean(x))/np.std(x)

df

df = pd.get_dummies(df, columns=['Tipo de Habitat', 'Presença de Algas', 'Nível de Poluição'])

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

df.columns.to_list()

for coluna in ['Temperatura da Água (°C)','Salinidade (ppt)', 'Profundidade (m)', 'pH']:
  if verifica_normalidade(df, coluna):
    df[coluna] = padronizar(df[coluna])#se for distribuição normal, padroniza
  else:#senão, normaliza
    df[coluna] = normalizar(df[coluna])

df

"""## b)KNN

e) Como a tarefa descrita é prever a presença ou ausência da espécie marinha (uma tarefa de classificação), o KNN é mais adequado. O K-Means seria apropriado se estivéssemos tentando agrupar amostras sem rótulos em grupos semelhantes.

"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

y = df['Presença de Espécie Marinha']
X = df.drop('Presença de Espécie Marinha', axis=1)

# Dividir o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X.shape[0]**0.5

knn = KNeighborsClassifier(n_neighbors=27)

#treinar o modelo kNN
knn.fit(X_train, y_train)

"""##d) Teste de acurácia dos dois modelos"""

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

"""##c) Rede Neural Multicamadas"""

entradas = df.drop('Presença de Espécie Marinha', axis=1)
entradas.head(1)

saida = df['Presença de Espécie Marinha']
saida.head(1)

redeneural = MLPClassifier(
    verbose=True,           # Para printar a "epóca"
    max_iter=10000,         # Máximo de interações
    tol=0.000001,           # Tolerância
    activation='relu',      # Função de ativação
    hidden_layer_sizes=(8, 5), # Camadas ocultas
    learning_rate_init=0.0001  # Taxa de aprendizado
)

redeneural.fit(X_train, y_train)

"""##d) Teste de acurácia dos dois modelos"""

y_pred_mlp = redeneural.predict(X_test)
accuracy_mlp = accuracy_score(y_test, y_pred_mlp)

print(f"Acurácia da Rede Neural: {accuracy_mlp}")



"""##f) [+1 bônus] Entregou além do esperado… me surpreenda"""

import seaborn as sb
sb.pairplot(df[['Temperatura da Água (°C)','Salinidade (ppt)', 'Profundidade (m)', 'pH','Presença de Espécie Marinha']], hue='Presença de Espécie Marinha')
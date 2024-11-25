# -*- coding: utf-8 -*-
"""Revisão_Python_aula4 26/02/24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Mie9npb3XlXk2Vm8-D8ZDpfp-bVnm5eH
"""

import pandas as pd
import matplotlib.pyplot as plt

import math

x = math.sqrt(4)

print(x)

print("Equação de primeiro grau")
def equacao(a,b,c):
  if a == 0:
    return -c/b
  else:
    delta =  b** - 4*a*c

    if delta == 0:
      print("Delta zero, apenas uma raiz real")
      return -b/(2*a)
    elif delta > 0:
      print("Delta positivo, duas raizes reais")
      x1 = (-b + delta**0.5)/(2*a)
      x2 = (-b - delta**0.5)/(2*a)
      return (x1, x2)
    else:
      print("Delta positivo, duas raizes imaginarias")
      x1 = (-b + delta**0.5)/(2*a)
      x2 = (-b - delta**0.5)/(2*a)
      return (x1, x2)

a = float(input("Digite a="))
b = float(input("Digite b="))
c = float(input("Digite c="))

print(equacao(a,b,c))

#visto da internet
# Valor inicial aplicado
vi = float( input('Valor inicial: ') )

# Rentabilidade mensagem, em %
i = float ( input('Rentabilidade mensal: ') )

# Transformando a porcentagem em valor numérico
i = i / 100

# Tempo de investimento
m = int( input('Meses que vai deixar rendendo: ') )

vf = vi * (1+i)**m

print('Valor apos ',m,' meses: R$ ',vf)

#Escrito por mim
print('Juros compostos')
c = float(input('Valor para ser investido:'))
j = float(input('Rentabilidade mensal:'))
j = i/100
t = int(input('Meses que vai deixar rendendo:'))
m = c * (1+j)**t
print('Valor após ' ,m, ' meses: R$' ,m)

#Professor
def juros_compostos (c, j , t):
  return c*(1+j)**t

c = float(input('Valor para ser investido:'))
j = float(input('Rentabilidade mensal:'))
t = int(input('Meses que vai deixar rendendo:'))
print(juros_compostos(c, t, j))

def juros_compostos (c, j , t):
  return c*(1+j)**t

c = float(input('Valor para ser investido:'))
j = float(input('Rentabilidade mensal:'))
t = int(input('Meses que vai deixar rendendo:'))
print(juros_compostos(c, t, j))

#Minha tentativa (primeira)
def aplicações_financeiras (c, j, t):
  return c*(1+j)**t

print('Informe os dados de investimento do primeiro aplicador')
c = float(input('Valor para ser investido:'))
j = float(input('Rentabilidade mensal:'))
t = int(input('Meses que vai deixar rendendo:'))
print('informe os dados de investimento do segundo aplicador')
c = float(input('Valor para ser investido:'))
j = float(input('Rentabilidade mensal:'))
t = int(input('Meses que vai deixar rendendo:'))

print(aplicações_financeiras(c, j, t))

#tentativa minha
def investidores (c, j, t):
  return c*(1+j)**36

c = input("investidor1 ou investidor2?")

investidor1 = {
    "nome": "João",
    "capital":10000,
    "investimentos": {
        "CDB": 0.35,
        "Ações": 0.12,
        "LCA": 0.33,
        "LCI": 0.20
    }
}

investidor2 = {
    "nome": "Maria",
    "capital":8000,
    "investimentos": {
        "CDB": 0.10,
        "Ações": 0.70,
        "FII": 0.20
    }
}

investidores = [investidor1, investidor2]

taxas = {
    "CDB": 0.01,
    "acoes": 1.0,
    "LCI": 0.02,
    "lca": 0.03,
    "FII":0.09
}

investidor1 = {
    "nome": "João",
    "capital":10000,
    "investimentos": {
        "CDB": 0.35,
        "Ações": 0.12,
        "LCA": 0.33,
        "LCI": 0.20
    }
}

investidor2 = {
    "nome": "Maria",
    "capital":8000,
    "investimentos": {
        "CDB": 0.10,
        "ações": 0.70,
        "FII": 0.20
    }
}

investidores = [investidor1, investidor2]

#professor (erro)
for pessoa in investidores:
  nome = pessoa['nome']
  capital = pessoa['capital']
  montante = 0
  for aplicacao, percentual in pessoa['investimentos'].items():
    montante += juros_compostos(capital*percentual, taxas[aplicacao],3)
    print(nome, "terá após 3 anos R${:.2f}".format(montante))

#Gráfico de multiplas linhas (passado pelo professor)
plt.plot([1,2,3], [1000, 2200, 3500], '-go') #linha com bolinhas verdes
plt.plot([1,2,3], [1100, 4900, 1000], ':', color='orange') #pontilhado laranja
plt.plot([1,2,3], [1200, 1500, 1000], '--r^')#trângulo vermelho tracejado
plt.plot([1,2,3], [1300, 2800, 4100], 'k--')#tracejado forte azul
plt.plot([1,2,3], [1400, 3000, 4300], ':s', color="pink") #pontilhado com quadrados rosas

plt.axis ( (1, 4, 1000, 7000))

plt.xlabel ("tempo (anos)")
plt.ylabel ("dinheiro (R$)")
plt.title ("dinheiro gasto no decorrer dos anos")

plt.show

#Gráfico de colunas (passada pelo professor)
faixaetaria = ["16-20", "21-25", "26-30"]
consumo = [1000, 800, 100]
plt.bar(faixaetaria,consumo, color='blue')
plt.xlabel("Faixa etária (anos)")
plt.ylabel ("Litros")
plt.title("Consumo anual de refrigerantes por faixa etária")
plt.show()

def juros_compostos (c, j , t):
  return c*(1+j)**t



#minha tentativa
investidor1 = {
    "nome": "Breno",
    "capital":10000,
    "investimento":{

    "CDB": 0.5}
  }

for pessoa in investidor1:
  nome = pessoa['nome']
  capital = pessoa['capital']
  montante = 0
   for aplicacao in pessoa['investimento'].items():
    montante += juros_compostos(capital*aplicacao,30)
    print(nome, "terá após 30 anos R${:.2f}".format(montante))
    investidores = [investidor1]

def  calcula_rentabilidade(c, j , t):
  return c*(1+j)**t

#professor
periodo = 30
capital_inicial = 10000
taxa_anual = 0.05
montante_final = []

for i in range(periodo+1):
  montante_final.append( calcula_rentabilidade(capital_inicial, taxa_anual, i))

eixo_x = list(range(periodo+1))
plt.plot(eixo_x, montante_final, "-bo")
plt.xlabel("anos")
plt.ylabel("patrimônio (R$)")
plt.title("Evolução patrimonial no decorrer dos anos")
plt.show()

capital = 2000
aporte = 500

taxa = 0.01 #ao mês
tempo = 5*12 #meses

montante = capital

for t in range (0, tempo+1):
  montante = montante*(1+taxa) + aporte
  print(t, 2500+aporte*t, aporte, montante)
  if t%12 == 0 and t>1:
    aporte += 500




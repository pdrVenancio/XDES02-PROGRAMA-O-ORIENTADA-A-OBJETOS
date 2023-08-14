""" 
n = int(input('digite um numero '))

#COMENTAR EM BLOCO shift + alt + A

n = input('digite um numero')       # input == scanf
print('o numero é {}'. format(n))   # DENTRO DA CHAVES PODEMOS MUDAR O ALINAMENTO DO TEXTO {:<} esquerda {:>} direita {:^} centralizar {:.2f} limita casas decimais
print(f'o numero e {n}')            # Melhor maneira

#FORÇANDO O TIPO 

int(input())
float(input())
bool(input()) # True / False
str(input())


5 ** 2 == 25 # ** ELVA O NUMERO A POTENCIA ESCOLHODA NO CASO 2
5 // 2 == 2  # // DIVISAO INTEIRA

#IMPORTAR BIBLIOTECAS

import math                   # importando a biblioteca inteira
from math import sqrt, floor  # Aqui importamos algo especifico da biblioteca

#FATIAMENTO DE STRING

frase = 'casa do pedro'

frase[0:3]   # Pega do elemento 0 ate o 3 (casa)
frase[0:6:2] # Pega do 0 ate o 6 porem saltando de 2 em 2 casas (cs)
frase[:5]    # do começo ate o 5
frase[5:]    # do elemento 5 ate o final
frase[-1]    # mostra o ultimo elemento

#CONDICIONAL

if n < 0:
    print('negativo')
else:
    print('positivo')

print('positivo' if n > 0 else 'negativo')

#else if == elif


#REPETIÇÃO

for contador in range(0,6): # Range(comeco, final, salto)
    print('nome')

c = 1
while c < 10:
        print(c)
        c += 1

# TUPLAS 

frase = ('casa','suco','de','uva') #Cara string é um elemento

# Listas

valores = [1,2,3,4,5,3,1]   

valores.insert(2, 0)    # inset(posicao, valor)

pessoas = list()        # cria uma lista em branco
pessoas = [['pedro',23], ['jamili', 30], ['jau',47]] # Listas dentro de listas

print(pessoas[0][0]) # vai printar pedro // por ser [estrutura][posição dentro da estrutura]

# DICIONARIOS

dados = dict()
dados = {'nome':'Pedro','idade':'20'} # Ao invesde 'pedro' ocupar a posição 0, vai ocupar a posição 'nome' // troca o indice

print(dados.values()) # Vao mostrar Pedro 20
print(dados.keys())   # Vai mostrar nome idade
print(dados.itens())  # Mostra os dois

# FUNCAO

def nomeDaFuncao(n): # n é o parametro
    print(n)
nomeDaFuncao(4)

def nomeDafuncao(*n) # *n para quando vc nao sabe a quantidade de parametros q vai passar

# MODULARIZAR 

import NomeDoarquivo    # Assim consigo importar funcoes de outros arquivos

from uteis import datas # Pasta "uteis" arqivo "datas" // Pacotes == Pastas
"""



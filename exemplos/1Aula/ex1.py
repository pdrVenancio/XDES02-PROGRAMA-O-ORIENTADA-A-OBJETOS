
#COMENTAR EM BLOCO shift + alt + A

n = input('digite um numero')       # input == scanf
print('o numero é {}'. format(n))   # DENTRO DA CHAVES PODEMOS MUDAR O ALINAMENTO DO TEXTO {:<} esquerda {:>} direita {:^} centralizar {:.2f} limita casas decimais

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





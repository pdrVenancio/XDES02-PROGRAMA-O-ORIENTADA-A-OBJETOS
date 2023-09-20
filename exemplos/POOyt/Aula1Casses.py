# AULA 35

#######---- CLASS ----########
from datetime import datetime

class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} nao esta falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, comida):
        if self.falando:
            print(f'{self.nome} nao pode comer falando')
            return
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return

        print(f'{self.nome} esta comendo {comida}')
        self.comendo = True
    
    def para_comer(self):
        if not self.comendo:
            print(f'{self.nome} ja nao esta comedo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

#### MAIN 

p1 = Pessoa('Pedro', 19)

p1.falar('casa')
p1.comer('pizza')
p1.parar_falar()
p1.comer('pizza2')


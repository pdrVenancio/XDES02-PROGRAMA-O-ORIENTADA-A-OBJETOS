#self = referece a instancia
#cls = referese a classe( pode ser qualquer nome que eu quiser )

class Pessoa:
    ano = 2023

    #construtor
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_de_nascimento(self):
        print(self.ano - self.idade)
    
    #meodo de classe // referente a classe em si
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimeto):
        idade = cls.ano - ano_nascimeto
        return cls(nome, idade)



#################################################################
#           MAIN

p1 = Pessoa.por_ano_nascimento("Pedro", 70)
print(p1)
print(p1.nome, p1.idade)
print(p1.idade)
p1.get_ano_de_nascimento()

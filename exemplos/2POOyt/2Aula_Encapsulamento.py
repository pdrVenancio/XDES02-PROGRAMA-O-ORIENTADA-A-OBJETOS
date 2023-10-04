#esta relacionado a permissão de uso

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade 
        self.__cpf = cpf #__ priva o (objeto) acesso de fora da classe

    def corre(self):
        print("estou correndo")

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('Bebendo...')

    def __apresentar_documento(self):# priva o metodo
        print(self.__cpf)


ronaldo = Pessoa('ronaldo', 23, '21312323')
#print(ronaldo.nome)
#print(ronaldo.idade)
ronaldo.beber('cerveja')
 
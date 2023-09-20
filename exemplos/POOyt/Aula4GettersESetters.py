class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    #PRECO
    #   getter - obtem
    @property
    def preco(self):
        return self._preco
    
    # setter - configura
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('RS', ''))
        self._preco = valor

    #NOME
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome =valor.title()


####################################
#       MAIN

p1 = Produto("camisa", 700)
p1.desconto(10)
print(p1.nome,p1.preco)

p1 = Produto("calca", 'RS840')
p1.desconto(30)
print(p1.nome, p1.preco)
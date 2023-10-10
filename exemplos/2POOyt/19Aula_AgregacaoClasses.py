from typing import Type

class Produto:
    def __init__(self, prod_nome, prof_valor) -> None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prof_valor

    def informacoes_produto(self):
        print(f'Produto: {self.__prod_nome}\tPreco: {self.__prod_valor}')

class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produto(self, produto: Type[Produto]):
        self.__produtos.append(produto)
    
    def finalizar_compra(self):
        print('Compras finalizadas!')
        for produto in self.__produtos:
            produto.informacoes_produto()
        self.__produtos = []



car = CarrinhoDeCompras()
monitor = Produto('monitor', 1000)
casa = Produto('casa', 1000)

car.adicionar_produto(monitor)
car.adicionar_produto(casa)
car.finalizar_compra()
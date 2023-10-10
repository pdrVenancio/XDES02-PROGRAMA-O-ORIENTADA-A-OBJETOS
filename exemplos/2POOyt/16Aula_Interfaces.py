#interfaces\formas.py
from abc import ABC, abstractstaticmethod
from typing import Type

class FormasInterface(ABC):
    
    @abstractstaticmethod
    def get_perimetro(self):
        pass

    @abstractstaticmethod
    def get_area(self):
        pass


#terrenos\quadrados.py
class TerrenoQuadrado(FormasInterface):

    def __init__(self, lado) -> None:
        self.lado = lado

    def get_perimetro(self):
        perimetro = self.lado * 4
        return perimetro

    def get_area(self):
        area = self.lado * self.lado
        return area

#terrenos\retangularllll.py   
class TerrenoRetangulo(FormasInterface):

    def __init__(self, largura, comprimento) -> None:
        self.largura = largura
        self.comprimento = comprimento

    def get_perimetro(self):
        perimetro = (self.largura) * 2 + (self.comprimento * 2)
        return perimetro

    def get_area(self):
        area = self.largura * self.comprimento
        return area

#Engenheiro.py

class Engenheiro:
    def __init__(self, nome) -> None:
        self.nome = nome

    def medir_perimetro(self, terreno: type[FormasInterface]):
        perimetro = terreno.get_perimetro()
        print(f'{self.nome} mediu o perimetro: {perimetro}')

    def medir_area(self, terreno: type[FormasInterface]):
        area = terreno.get_area()
        print(f'{self.nome} mediu a area: {area}')


eng = Engenheiro('Caio')
teQ = TerrenoQuadrado(5)
teR = TerrenoRetangulo(2,4)

eng.medir_area(teQ)
eng.medir_perimetro(teQ)

eng.medir_area(teR)
eng.medir_perimetro(teR)





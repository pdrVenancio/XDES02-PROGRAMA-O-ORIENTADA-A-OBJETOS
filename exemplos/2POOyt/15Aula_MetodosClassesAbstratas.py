#Metodo abstrato: toda vez q vc tem uma herança é preciso implementar nas classes filhas esse metodo abstrato

from abc import ABC, abstractclassmethod

class AbstrectClass(ABC):
    def __init__(self) -> None:
        self.atributo = 'Ola mundo'
    
    def metodo(self, elemento: str):
        print(elemento)
    
    @abstractclassmethod
    def metodo_abstrato(self):
        pass


class Filha(AbstrectClass):
    def apresenta_metodo(self):
        print(self.atributo)

    def metodo_abstrato(self):
        print('implementando metodo abs')


filha = Filha()
filha.apresenta_metodo()
filha.metodo('Estou aqui')
filha.metodo_abstrato()

#abstractclass = AbstrectClass()
#abstractclass.metodo('Fazendo algo')
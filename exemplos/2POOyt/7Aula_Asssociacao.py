#Associando duas classe passando os objetos em si
from typing import Type

class Interruptor:
    def __init__(self,comodo) -> None:
        self.__comodo = comodo

    def acender(self):
        print(f'acendendo {self.__comodo}')
    def apagar(self):
            print(f'apagar {self.__comodo}')

class Pessoa:
     
    def acender(self, interruptor: Type[Interruptor]):# como se interruptor fosse um objeto
        interruptor.acender()
    
    def apagar(self, interruptor: Type[Interruptor]):
        interruptor.apagar()
    
    def dormir(self):
         print('dormindo... ZZZzzzZZZzzZZZZzzZzZzZ')


lhama = Pessoa()
interruptor_quarto = Interruptor('quarto')

interruptor_quarto.acender()
lhama.acender(interruptor_quarto)
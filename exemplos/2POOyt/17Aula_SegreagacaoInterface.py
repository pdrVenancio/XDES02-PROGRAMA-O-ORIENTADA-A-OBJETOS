#Usar uma interface mais especifica ao invez de uma mais generalizada

from abc import ABC, abstractclassmethod

#interface.py
class AveVoadora(ABC):

    @abstractclassmethod
    def comer(self):
        raise 'deu merda'

    @abstractclassmethod
    def voar(self):
        raise 'deu merda'
    
    @abstractclassmethod
    def gritar(self):
        raise 'deu merda'
    
class AveNaoVoadora(ABC):

    @abstractclassmethod
    def comer(self):
        raise 'deu merda'
    
    @abstractclassmethod
    def gritar(self):
        raise 'deu merda'
    
    
#aves.py

class Canario(AveVoadora):
    def comer(self):
        print('Comendo...')
    
    def voar(self):
        print('Voando...')
    
    def gritar(self):
        print('Gritando...')


class Pinguim(AveNaoVoadora):
    def comer(self):
        print('Comendo...')
    
    def gritar(self):
        print('Gritando...')

    def __acasalar(self):
        print('ain ainnnnn toma vai')

#run.py
canario = Canario()
ping = Pinguim()

canario.voar()
ping.comer()

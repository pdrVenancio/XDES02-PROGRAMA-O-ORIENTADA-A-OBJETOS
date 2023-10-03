from abc import ABC, abstractmethod
class banco(ABC):
    def __init__(self, nConta, nome,  saldo):
        self.__nConta = nConta
        self.__nome = nome
        self.__saldo = saldo

    


class contCorrente(banco):

class contCorrenteLimite(banco):
    def __init__(self, nConta, nome, saldo, limite):
        super().__init__(nConta, nome, saldo)
        self.__limite = limite

class contPoupanca(banco):
    def __init__(self, nConta, nome, saldo, aniversario):
        super().__init__(nConta, nome, saldo)
        self.__aniversario = aniversario
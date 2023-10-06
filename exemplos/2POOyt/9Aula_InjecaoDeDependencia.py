# Um objeto depende de outro objeto

from typing import Type

class Casa:
    def __init__(self) -> None:
        self.__endereco = 'Rua Tamoio'
    
    def acender_luzes(self):
        print("acendendo")
    
    def get_endereco(self):
        return self.__endereco
    
class Pessoa:

    def __init__(self, nome, local: Type[Casa]) -> None:
        self.__nome = nome
        self.__local = local

    def entrar_local(self):
        self.__local.acender_luzes()

    def apresentar_local(self):
        endereco = self.__local.get_endereco()
        print(endereco)


casa_amigo = Casa()
ana = Pessoa('Ana', casa_amigo)

ana.entrar_local()
ana.apresentar_local()
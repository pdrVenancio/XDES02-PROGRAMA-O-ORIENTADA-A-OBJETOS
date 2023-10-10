from typing import Type
from abc import ABC, abstractclassmethod

#Interface.py
class Repositorio:

    @abstractclassmethod
    def inserir(self, dado):
        pass
    @abstractclassmethod
    def deletar(self, dado):
        pass

#mysql_repositorio.py

class MySqlRepositorio(Repositorio):

    def inserir(self, dado):
        print(f'Inserindo {dado} no banco...')

    def deletar(self, dado):
        print(f'Removendo {dado} do banco...')


# run.py

class Usuario:
    def __init__(self, repositorio: type[Repositorio]) -> None:
        self.__repositorio = repositorio

    def armazenar_dado(self, dado):
        self.__repositorio.inserir(dado)

    def remover_dado(self, dado):
        self.__repositorio.deletar(dado)


use = Usuario(MySqlRepositorio())
use.armazenar_dado(23)

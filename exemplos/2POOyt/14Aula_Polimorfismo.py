# Mudar o comportamento do objeto

from typing import Dict, Type

#repositorio.py
class Repositorio:
    def select(self, nome):
        return {"nome": nome, "idade":32}
    
    def inserir(self, nome, idade):
        print(f'Inserindo dados {nome} {idade}')
        return {"nome": nome, "idade": idade}

#insersor.py
class Insersor:
     
    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repo = repositorio
    
    def inserir_dado(self, nome: str, idade: int):
        registro = self.__repo.select(nome)
        if registro:
            raise Exception('O registro ja existe')

        novo_regitro = self.__repo.inserir(nome, idade)
        return novo_regitro
        
#run.py
class RepositorioFake(Repositorio):
    def __init__(self) -> None:
        super().__init__()
    
    def select(self, nome: int):
        return None
    

repo = RepositorioFake()
insersor = Insersor(repo)

data = insersor.inserir_dado('Pedro', 21)
print(data)
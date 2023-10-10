from typing import Type
#banco de dados.py
class Conexao:

    def conectar(self):
        print('Conectando....')

    def desconectar(self):
        print('Desconectando...')
    
class MySQLrepo(Conexao):
    def __init__(self) -> None:
        super().__init__()

    def select(self):
        self.conectar()
        print('SELECT *FROM casa')


class CasoDeUso:
    def buscar(self, db_repo):
        db_repo.select()


#run.py
#Quebra do princio de Liskov
class PessoaA:
    def se_apresentar(self):
        print('ola aou pessoa 1')

class PessoaB(PessoaA):
    def __init__(self) -> None:
        super().__init__()
    
    def se_apresentar(self):
        print('mudando o metodo se_apresentar')
    

#pessoa = PessoaA()
#pessoa.se_apresentar()

# pessoa2 = PessoaB()
# pessoa2.se_apresentar()

#zoologico.py

# Ese é o principio de Liskov onde nenhuma classe/subclasse altera um petodo da classe mae

class Animal:
    def comer(self):
        print('Comendo...')
    
    def dormir(self):
        print('Dormindo...')
    
    def andar(self):
        print('Andando...')

class Aves(Animal):
    def __init__(self) -> None:
        super().__init__()

    def cantar(self):
        print('Cantando...')

class Pinguim(Aves):
    def __init__(self) -> None:
        super().__init__()

    def escorregar(self):
        print('Escorregando no gelo...')

class Pessoa:
    def observar(sel, animal: Type[Animal]):
        animal.comer()

roberto = Pessoa()
pinguin = Animal()
roberto.observar(pinguin)
        
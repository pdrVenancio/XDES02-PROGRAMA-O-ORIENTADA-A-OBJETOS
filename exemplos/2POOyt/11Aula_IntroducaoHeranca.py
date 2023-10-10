#classe mae e clasee filha 
#erda os metodos da classe mae 

class Mae:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'venancio'

    def comer(self):
        print('Come come')
    
    def estudar(self):
        print('Tudando')

class Filha(Mae):
    def __init__(self,  endereco) -> None:
        super().__init__(endereco)  #referencia ao init da classe mae
    
    def brincar(self, brinquedo):
        print(f'Estou brincando com {brinquedo}')

class Neta(Filha):
    def __init__(self, endereco) -> None:
        super().__init__(endereco)
    




Ana = Mae('jao pessoa')
clara = Filha('casa do papa')
clara.brincar('boneca')



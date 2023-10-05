#nao tem uma contesto pre definido
#utilizar como espicificador

class MinhaClasse:

    def __init__(self, estado: bool) -> None:
        self.estado = estado
    
    @staticmethod# nao tem  acesso a outros elementos da classe 
    def metodo_estatico():
        print('metodo estatico')

ob = MinhaClasse(True)
ob.metodo_estatico()
MinhaClasse.metodo_estatico()  # nao preciso do obj para usar a funcionalidade dentro da clss 

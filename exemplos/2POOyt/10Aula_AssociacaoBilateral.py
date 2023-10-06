# casa.py

class Casa:
    def __init__(self) -> None:
        self.__endereco = "Rua duque de caxias"
        self.__proprietario = None

    def acender_luzes(self):
        print('acendeu..')

    def get_endereco(self):
        return self.__endereco
    
    def set_proprietario(self, proprietario):
        self.__proprietario = proprietario

    
    def get_proprietario(self):
        return self.__proprietario
    
# pessoa.py

class Pessoa:

    def __init__(self, nome) -> None:
        self.__local = None
        self.__nome = nome

    def entrar_no_local(self):
        self.__local.acender_luzes()

    def apresentar_local(self):
        endereco = self.__endereco.get_endereco()
        print(endereco)

    def se_apresentar(self):
        print(f'ola, eu sou {self.__nome}')


    def set_local(self, local):
        self.__local =  local

    def get_local(self):
        return self.__local

#   main 
#   importar outros arquivos
casa_ana = Casa()
ana = Pessoa('ana')

ana.set_local(casa_ana)
casa_ana.set_proprietario(ana)

proprietario = casa_ana.get_proprietario()
proprietario.se_apresentar()
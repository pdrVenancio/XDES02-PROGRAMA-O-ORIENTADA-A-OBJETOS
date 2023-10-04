class Loja:

    tarifa = 1.03

    def __init__(self, endereco: str) -> None:
        self.__endereco = endereco

    def apresentar_endereco(self):
        print(self.__endereco)
    
    @classmethod
    def vender(cls)-> int:
        return 40 * cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: float) -> None:
        cls.tarifa = nova_tarifa


loja_praia = Loja('Praia')
loja_centro = Loja('centro')

loja_praia.apresentar_endereco()

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.alterar_tarifa(5000)


print(loja_praia.vender())
print(loja_centro.vender())







# class MinhaClasse:

#     estatico = 'Pedro'# Variavel de classe
                       

#     def __init__(self, estado: bool) -> None:
#         self.estado = estado
    
#     def print_estatico(self):
#         print(self.estatico) #self faz referencia ao ob1

#     @classmethod
#     def mudar_estatico(cls, pl):
#         cls.estatico = pl
            
# ob1 = MinhaClasse(True)
# ob1.mudar_estatico('casa')
# ob1.print_estatico()



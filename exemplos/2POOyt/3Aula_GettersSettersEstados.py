class Alarme:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self)->bool:
        return self.__estado
    
    def set_estado(self, valor: bool)-> None:
        if isinstance(valor, bool):
            self.__estado = valor



# #continua sendo uma forma de encapsulamento

# class Pessoa:
#     def __init__(self, nome: str, idade: int) -> None:
#         self.nome = nome
#         self.idade = idade
    
#     def dirigir(self, veiculo: str) -> None:#nao retorna nada
#         print(f'dirigindo um {veiculo}')
    
#     def cantar(self) -> None:
#         print('lalalala')
    
#     def apresentar_idade(self) -> int:#por retornar um inteiro
#         return self.idade
    

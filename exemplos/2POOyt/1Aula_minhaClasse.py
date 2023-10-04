class ControleRemoto():
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print("canal avancado")
    
    def voltar_canal(self):
        print("canal voltou")

    def escolher_canal(self, canal):
        print(f'Alterar para o canal {canal}')

controle_sala = ControleRemoto('sansung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

    
controle_quarto = ControleRemoto('LG', 'quarto')
print(controle_quarto.comodo)
print(controle_quarto.televisao)







"""""
class Minhaclasse:
    def __init__(self, att):
        self.meu_atributo = "ola mundo"
        self.meu_atributo2 = att

    def meu_metodo(self):#self: se referencia a classe q esta indentado 
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num, mult):
        return num * mult

objeto = Minhaclasse(3)
objeto.meu_metodo()
#result = objeto.meu_metodo2(3, 3)
#print(result)
#print(objeto.meu_atributo2)
"""""
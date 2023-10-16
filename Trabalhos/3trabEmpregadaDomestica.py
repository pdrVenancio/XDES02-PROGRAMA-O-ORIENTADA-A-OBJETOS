#NOME: Pedro Venancio dos Santos MATRICULA:2023010066

from abc import ABC, abstractmethod

class EmpregadaDomestica(ABC):

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__tel = telefone

    @abstractmethod
    def getSalario(self):
        pass

    @property
    def nome(self):
        return self.__nome
    
    @property
    def tel(self):
        return self.__tel

class Horista(EmpregadaDomestica):

    def __init__(self, horaTrab, valorHora, nome, telefone):
        super().__init__(nome, telefone)
        self.__horaTrab = horaTrab
        self.__valorHora = valorHora

    @property
    def valorHora(self):
        return self.__valorHora
    
    @valorHora.setter
    def valorHora(self, valorHora):
        self.__valorHora = valorHora
    
    def getSalario(self):
        return self.valorHora * self.__horaTrab

class Diarista(EmpregadaDomestica):
    def __init__(self, diasTrab, valorDia, nome, telefone):
        super().__init__(nome, telefone)
        self.__diasTrab = diasTrab
        self.__valorDia = valorDia

    @property
    def valorDia(self):
        return self.__valorDia

    @valorDia.setter
    def valorDia(self, valorDia):
        self.__valorDia = valorDia
    
    def getSalario(self):
        return self.valorDia * self.__diasTrab 

class Mensalista(EmpregadaDomestica):
    def __init__(self, valorMensal, nome, telefone):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    @property
    def valorMensal(self):
        return self.__valorMensal

    @valorMensal.setter
    def valorMensal(self, valorMensal):
        self.__valorMensal = valorMensal
    
    def getSalario(self):
        return self.valorMensal


if __name__ == '__main__':
    e1 = Horista(160, 12, 'Maria', 35999955555)
    e2 = Diarista(20, 65, 'Paulo', 3588886666)
    e3 = Mensalista(1200, 'Ana', 3577772222)
    
    empregadas = [e1, e2, e3]
    for emp in empregadas:
        print(f'Nome: {emp.nome} \nSalário: {emp.getSalario()}\n')

    marba = e1.getSalario()

    for emp in empregadas:
        if emp.getSalario() < marba:
            telMarab = emp.tel
            nomeMarba = emp.nome
            marba = emp.getSalario()


    print(f'\n\n\tEMPREGADA MAIS BARATA\n\nNome: {nomeMarba}\nTelefone: {telMarab}\nSalario: {marba}\n')


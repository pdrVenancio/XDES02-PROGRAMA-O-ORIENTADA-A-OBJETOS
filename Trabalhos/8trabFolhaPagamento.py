from abc import ABC, abstractmethod

class PontoFunc:
    def __init__(self, mes, ano, nrfaltas, nrAtrasos) -> None:
        self.__mes = mes
        self.__ano = ano
        self.__nrFaltas = nrfaltas
        self.__nrAtrasos = nrAtrasos

    @property
    def get_mes(self):
        return self.__mes
    
    @property
    def get_ano(self):
        return self.__ano
    
    @property
    def lanca_faltas(self):
        return self.__nrFaltas
    
    @property
    def lanca_atrsos(self):
        return self.__nrAtrasos
        

class Funcionario(ABC):
    def __init__(self, cod, nome) -> None:
        self.__cod = cod
        self.__nome = nome
        self.__pontoMensal = []

    @property
    def get_cod(self):
        return self.__cod
    
    @property
    def get_nome(self):
        return self.__nome
    
    @property
    def getPontoMensal(self):
        return self.__pontoMensal
    
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        ponto = {
            'mes': mes,
            'ano': ano,
            'faltas': faltas,
            'atrasos': atrasos
        }
        self.__pontoMensal.append(ponto)

    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self.__pontoMensal:
            if ponto['mes'] == mes and ponto['ano'] == ano:
                ponto['faltas'] = faltas

    def lancaAtrasos(self, mes, ano, atrasos):
        for ponto in self.__pontoMensal:
            if ponto['mes'] == mes and ponto['ano'] == ano:
                ponto['atrasos'] = atrasos

    def imprimeFolha(self, mes, ano):
        for ponto in self.__pontoMensal:
            if ponto['mes'] == mes and ponto['ano'] == ano:
                salario = self.calculaSalario(mes, ano)
                bonus = self.calculaBonus(mes, ano)
                print(f'codigo: {self.__cod}\nnome: {self.__nome}\nSalario Liquido: {salario:.2f}\nBonus: {bonus:.2f} ')
        

    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass

    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass



class Professor(Funcionario):
    def __init__(self, cod, nome, titulacao, salarioHr: float, nroAulas) -> None:
        super().__init__(cod, nome)
        self.__titulacao = titulacao
        self.__salarioHr = salarioHr
        self.__nroAulas = nroAulas
   
    @property
    def getTitulacao(self):
        return self.__titulacao
    
    @property
    def getSalarioHora(self):
        return self.__salarioHr
    
    @property
    def getNrAulas(self):
        return self.__nroAulas

    def calculaSalario(self, mes, ano):
        for ponto in self.getPontoMensal:
            if ponto['mes'] == mes and ponto['ano'] == ano:
                nro_faltas = ponto['faltas']
                return self.__salarioHr * self.__nroAulas - self.__salarioHr * nro_faltas
              
    def calculaBonus(self, mes, ano):
        for ponto in self.getPontoMensal:
            if ponto['mes'] == mes and ponto['ano'] == ano:
                nro_atrasos = ponto['atrasos']
                return (0.1 - nro_atrasos/100) * self.calculaSalario(mes, ano)

class TecAdmin(Funcionario):
    def __init__(self, cod, nome,  funcao, salario: float) -> None:
        super().__init__(cod, nome)
        self.__salario = salario
        self.__funcao = funcao

    @property
    def getFuncao(self):
        return self.__funcao
    
    @property
    def getSalario(self):
        return self.__salario

    def calculaSalario(self, mes, ano):
        for ponto in self.getPontoMensal:
            if ponto['mes'] == mes and ponto['ano'] == ano:
                nro_faltas = ponto['faltas']
                return self.__salario - (self.__salario / 30) * nro_faltas

    def calculaBonus(self, mes, ano):
        for ponto in self.getPontoMensal:
            if ponto['mes'] == mes and ponto['ano'] == ano:
                nro_atrasos = ponto['atrasos']
                return (0.08 - nro_atrasos/100)* self.calculaSalario(mes, ano) 


if __name__=="__main__":
    funcionarios=[]
    prof = Professor(1,"Joao","Doutor",45.35,32)
    prof.adicionaPonto(4,2021,0,0)
    prof.lancaFaltas(4,2021,2)
    prof.lancaAtrasos(4,2021,3)
    funcionarios.append(prof)

    tec = TecAdmin(2,"Pedro","AnalistaContábil",3600)
    tec.adicionaPonto(4,2021,0,0)
    tec.lancaFaltas(4,2021,3)
    tec.lancaAtrasos(4,2021,4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4,2021)
        print()
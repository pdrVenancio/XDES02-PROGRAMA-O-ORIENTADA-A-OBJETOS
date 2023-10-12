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
    def get_nrFaltas(self):
        return self.__nrFaltas
    
    @property
    def get_nrAtrasos(self):
        return self.__nrAtrasos
    
    def lanca_faltas(self, nrFaltas):
        self.__nrFaltas += nrFaltas
    
    def lanca_atrasos(self, nrAtrasos):
        self.__nrAtrasos += nrAtrasos


class Funcionario(ABC):
    def __init__(self, cod, nome):
        self.__cod = cod
        self.__nome = nome
        self.__getPontoMensal = []

    @property
    def get_cod(self):
        return self.__cod
    
    @property
    def get_nome(self):
        return self.__nome
    
    @property
    def getPontoMensal(self):
        return self.__getPontoMensal
    
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self.__getPontoMensal.append(PontoFunc(mes, ano, faltas, atrasos))

    def lanca_faltas(self, mes, ano, faltas):
        lista = self.__getPontoMensal
        
        for ficha in lista:
            if ficha.get_mes == mes and ficha.get_ano == ano:
                ficha.lanca_faltas(ficha.get_nrFaltas + faltas)
                break

    def lanca_atrasos(self, mes, ano, atrasos):
        lista = self.__getPontoMensal
        
        for ficha in lista:
            if ficha.get_mes == mes and ficha.get_ano == ano:
                ficha.lanca_atrasos(atrasos)
                break

    def imprimeFolha(self, mes, ano):
            print(f'codigo: {self.__cod}\nnome: {self.__nome}\nSalario Liquido: {self.calculaSalario(mes, ano):.2f}\nBonus: {self.calculaBonus(mes, ano):.2f} ')
        

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
        lista = self.getPontoMensal
        total_faltas = 0
        for ponto in lista:
                
            if ponto.get_mes == mes and ponto.get_ano == ano:
                total_faltas = ponto.get_nrFaltas
                break
                
        return self.__salarioHr * self.__nroAulas - self.__salarioHr * total_faltas
              
    def calculaBonus(self, mes, ano):
        lista = self.getPontoMensal
        nro_atrasos = 0
        for ponto in lista:
            if ponto.get_mes == mes and ponto.get_ano == ano:
                nro_atrasos = ponto.get_nrAtrasos
                break
    
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
        lista = self.getPontoMensal
        total_faltas = 0
        for ponto in lista:
                
            if ponto.get_mes == mes and ponto.get_ano == ano:
                total_faltas = ponto.get_nrFaltas
                break
                
        return self.__salario - ((self.__salario/30)* total_faltas)
    
    def calculaBonus(self, mes, ano):
        lista = self.getPontoMensal
        nro_atrasos = 0
        for ponto in lista:
            if ponto.get_mes == mes and ponto.get_ano == ano:
                nro_atrasos = ponto.get_nrAtrasos
                break
        if nro_atrasos > 8:
            nro_atrasos = 8
            
        return ((8 - nro_atrasos)/100) * self.calculaSalario(mes, ano) 


if __name__=="__main__":
    funcionarios=[]
    prof = Professor(1,"Joao","Doutor",45.35,32)
    prof.adicionaPonto(4,2021,0,0)
    prof.lanca_faltas(4,2021,2)
    prof.lanca_atrasos(4,2021,3)
    funcionarios.append(prof)

    tec = TecAdmin(2,"Pedro","AnalistaContábil",3600)
    tec.adicionaPonto(4,2021,0,0)
    tec.lanca_faltas(4,2021,3)
    tec.lanca_atrasos(4,2021,4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4,2021)
        print()
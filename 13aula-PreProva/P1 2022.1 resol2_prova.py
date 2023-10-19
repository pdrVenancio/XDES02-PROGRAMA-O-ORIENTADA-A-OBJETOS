from abc import ABC, abstractmethod


class Trabalhador(ABC):
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome
        self.__dependentes = []

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def dependentes(self):
        return self.__dependentes

    def insereDependente(self, dependente):
        self.__dependentes.append(dependente)

    @abstractmethod
    def calculaPgmento(self, mes):
        ...

    @abstractmethod
    def imprimeRecibo(self, mes):
        ...


class Diarista(Trabalhador):
    def __init__(self, cpf, nome, valorDiaria):
        super().__init__(cpf, nome)
        self.__valorDiaria = valorDiaria
        self.__listaDiaria = []

    @property
    def valorDiaria(self):
        return self.__valorDiaria

    @property
    def listaDiaria(self):
        return self.__listaDiaria

    def adicionaDiaria(self, diaria):
        self.__listaDiaria.append(diaria)

    def obtemValorAuxilio(self):
        valorAuxilio = 0
        for dependente in self.dependentes:
            if (dependente.idade < 6):
                valorAuxilio += 100

        return valorAuxilio

    def calculaPgmento(self, mes):
        valorPagamento = 0
        for diaria in self.__listaDiaria:
            if (diaria.mes == mes):
                if (diaria.temRefeicao):
                    valorPagamento -= 10.0
                if (diaria.temAtraso):
                    valorPagamento -= (valorPagamento * 0.1)

        return valorPagamento

    def imprimeRecibo(self, mes):
        ...


class Empreiteiro(Trabalhador):
    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)
        self.__listaEmpreito = []

    @property
    def listaEmpreito(self):
        return self.__listaEmpreito

    def adicionaEmpreito(self, empreito):
        self.__listaEmpreito.append(empreito)

    def calculaPgmento(self, mes):
        ...

    def imprimeRecibo(self, mes):
        ...


class Diaria:
    def __ini__(self, dia, mes, ano, temRefeicao, temAtraso):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__temRefeicao = temRefeicao
        self.__temAtraso = temAtraso

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @property
    def temRefeicao(self):
        return self.__temRefeicao

    @property
    def temAtraso(self):
        return self.temAtraso


class Dependente:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Empreito:
    def __init__(self, mes, ano, descricao, valor, atrasoEntrega):
        self.__mes = mes
        self.__ano = ano
        self.__descricao = descricao
        self.__valor = valor
        self.__atrasoEntrega = atrasoEntrega

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

    @property
    def atrasoEntrega(self):
        return self.__atrasoEntrega

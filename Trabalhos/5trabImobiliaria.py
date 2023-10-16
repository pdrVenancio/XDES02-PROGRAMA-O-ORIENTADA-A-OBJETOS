#NOME: Pedro Venancio dos Santos MATRICULA:2023010066

class Venda:
    def __init__(self, codigo_imovel, mes, ano, valor):
        self.codigo_imovel = codigo_imovel
        self.mes = mes
        self.ano = ano
        self.valor = valor

class Vendedor:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.vendas = []

    def adicionaVenda(self, codigo_imovel, mes, ano, valor):
        venda = Venda(codigo_imovel, mes, ano, valor)
        self.vendas.append(venda)

    def calculaRenda(self, mes, ano):
        pass 

    def getDados(self):
        pass  

class Contratado(Vendedor):
    def __init__(self, codigo, nome, salario, numero_carteira):
        super().__init__(codigo, nome)
        self.salario = salario
        self.numero_carteira = numero_carteira

    def calculaRenda(self, mes, ano):
        comissao = 0
        for venda in self.vendas:
            if venda.mes == mes and venda.ano == ano:
                comissao += venda.valor * 0.01
        return self.salario + comissao

    def getDados(self):
        return f"Nome: {self.nome}\nNro Carteira: {self.numero_carteira}"

class Comissionado(Vendedor):
    def __init__(self, codigo, nome, cpf, percentual_comissao):
        super().__init__(codigo, nome)
        self.cpf = cpf
        self.percentual_comissao = percentual_comissao / 100  # Convertendo para a porcentagem decimal

    def calculaRenda(self, mes, ano):
        comissao = 0
        for venda in self.vendas:
            if venda.mes == mes and venda.ano == ano:
                comissao += venda.valor * self.percentual_comissao
        return comissao

    def getDados(self):
        return f"Nome: {self.nome}\nNro CPF: {self.cpf}"

if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)

    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)

    listaFunc = [funcContratado, funcComissionado]

    for func in listaFunc:
        print(func.getDados())
        print("Renda no mês 3 de 2022:")
        print(func.calculaRenda(3, 2022))
 

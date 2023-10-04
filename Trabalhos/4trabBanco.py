from abc import ABC, abstractmethod
from datetime import datetime

class Conta(ABC):
    def __init__(self, numero_conta, nome_correntista, saldo):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        self.transacoes = []

    @abstractmethod
    def ImprimirExtrato(self):
        pass

    def Deposito(self, valor, descricao):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append((datetime.now(), valor, descricao))
        else:
            print("Valor de depósito deve ser positivo.")

    @abstractmethod
    def Retirada(self, valor, descricao):
        pass

class ContaComum(Conta):
    def ImprimirExtrato(self):
        print(f"Conta Comum - Número: {self.numero_conta}, Correntista: {self.nome_correntista}")
        print("Transações:")
        for data, valor, descricao in self.transacoes:
            print(f"{data.strftime('%Y-%m-%d %H:%M:%S')}: {descricao} - R${valor:.2f}")
        print(f"Saldo: R${self.saldo:.2f}")

    def Retirada(self, valor, descricao):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append((datetime.now(), -valor, descricao))
        else:
            print("Saldo insuficiente para a retirada.")

class ContaLimite(Conta):
    def __init__(self, numero_conta, nome_correntista, saldo, limite):
        super().__init__(numero_conta, nome_correntista, saldo)
        self.limite = limite

    def ImprimirExtrato(self):
        print(f"Conta Limite - Número: {self.numero_conta}, Correntista: {self.nome_correntista}")
        print("Transações:")
        for data, valor, descricao in self.transacoes:
            print(f"{data.strftime('%Y-%m-%d %H:%M:%S')}: {descricao} - R${valor:.2f}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Limite: R${self.limite:.2f}")

    def Retirada(self, valor, descricao):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.transacoes.append((datetime.now(), -valor, descricao))
        else:
            print("Saldo insuficiente para a retirada.")

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, nome_correntista, saldo, aniversario_conta):
        super().__init__(numero_conta, nome_correntista, saldo)
        self.aniversario_conta = aniversario_conta

    def ImprimirExtrato(self):
        print(f"Conta Poupança - Número: {self.numero_conta}, Correntista: {self.nome_correntista}")
        print("Transações:")
        for data, valor, descricao in self.transacoes:
            print(f"{data.strftime('%Y-%m-%d %H:%M:%S')}: {descricao} - R${valor:.2f}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Aniversário da Conta: {self.aniversario_conta}")

    def Retirada(self, valor, descricao):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append((datetime.now(), -valor, descricao))
        else:
            print("Saldo insuficiente para a retirada.")

# Código de teste
if __name__ == '__main__':
    conta_comum = ContaComum(1001, "João", 1000.0)
    conta_limite = ContaLimite(2001, "Maria", 1500.0, 500.0)
    conta_poupanca = ContaPoupanca(3001, "Carlos", 2000.0, "10/03")

    conta_comum.Deposito(500.0, "Depósito inicial")
    conta_comum.Retirada(200.0, "Pagamento de conta")
    conta_comum.Deposito(300.0, "Depósito adicional")

    conta_limite.Deposito(1000.0, "Depósito inicial")
    conta_limite.Retirada(2200.0, "Compra com cartão")

    conta_poupanca.Deposito(800.0, "Depósito inicial")
    conta_poupanca.Retirada(150.0, "Retirada de emergência")

    contas = [conta_comum, conta_limite, conta_poupanca]

    for conta in contas:
        conta.ImprimirExtrato()
        print("="*40)

import tkinter
from tkinter import messagebox
import cliente

class NotaFiscal():
    #produtos nao deveria ser uma lista???
  
    def __init__(self, numero, cliente, produtos, dataEmissao, valorTotal):
        self.__numero = numero  # Número único da nota fiscal
        self.__cliente = cliente  # Informações do cliente (pode ser um objeto da classe Cliente)
        self.__produtos = produtos  # Lista de produtos na nota fiscal (cada item pode ser um objeto da classe Produto)
        self.__dataEmissao = dataEmissao  # Data de emissão da nota fiscal
        self.__valorTotal = valorTotal  # Valor total da nota fiscal

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor):
        self.__numero = valor

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor

    @property
    def produtos(self):
        return self.__produtos
    
    @produtos.setter
    def produtos(self, valor):
        self.__produtos = valor

    @property
    def dataEmissao(self):
        return self.__dataEmissao
    
    @dataEmissao.setter
    def dataEmissao(self, valor):
        self.__dataEmissao = valor

    @property
    def valorTotal(self):
        return self.__valorTotal

    @valorTotal.setter
    def valorTotal(self, valor):
        self.__valorTotal = valor

class ViewEmitirNota(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Emitir nota Fiscal")
        self.controle = controle

        self.frameCpf = tkinter.Frame(self)
        self.frameCpf.pack()
        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()

        self.labelCpf = tkinter.Label(self.frameCpf, text="CPF:")
        self.labelCpf.pack(side="left")
        self.inputCpf = tkinter.Entry(self.frameCpf, width=20)
        self.inputCpf.pack(side="left")
        self.buttonCpf = tkinter.Button(self.frameButton, text="Buscar", command=self.controle.buscarCpf)
        self.buttonCpf.pack(side="left")

    def mostraSucesso(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def mostraErro(self, titulo, msg):
        messagebox.showerror(titulo, msg)

class CtrlNotaFiscal():

    def __init__(self, controleprincipal):
        self.controlePrincipal = controleprincipal
        self.listaProdutos = controleprincipal.ctrlProduto.getListaProduto() #pega a lista de todos os produtos registrados

    def emitirNota(self):
        self.viewEmitirNota = ViewEmitirNota(self)

    def buscarCpf(self):
        cpf = self.viewEmitirNota.inputCpf.get()
        if cpf == "":
            self.viewEmitirNota.mostraErro("Erro", "Digite um CPF")
        else:
            for c in cliente.CtrlCliente.listaClientes:
                if c.cpf == cpf:
                    self.viewEmitirNota.labelCpf.config(text="Cliente: ")
                    self.viewEmitirNota.inputCpf.config(state="disabled")
                    break
            else:
                self.viewEmitirNota.mostraErro("Erro", "Cliente não encontrado!\nCadastre um cliente antes de prosseguir")
                return

        
import tkinter
from tkinter import messagebox, ttk
class Peixe():
    def __init__(self, nome, preco) -> None:
        self.__nome = nome
        self.__preco = preco


    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

class ItemComanda():
    def __init__(self, nome, preco, peso) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__peso = peso


    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def peso(self):
        return self.__peso
    
class Comanda():
    def __init__(self, itens) -> None:
        self.__itens = itens

    @property
    def itens(self):
        return self.__itens
    

    
class ViewCadastro(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("")
        self.controle = controle 

        self.frameNomePeixe = tkinter.Frame(self)
        self.frameNomePeixe.pack()
        self.labelNomePeixe = tkinter.Label(self.frameNomePeixe, text="NomePeixe: ")
        self.labelNomePeixe.pack(side="left")
        self.inputNomePeixe = tkinter.Entry(self.frameNomePeixe, width=20)
        self.inputNomePeixe.pack(side="left")

        self.framePreco = tkinter.Frame(self)
        self.framePreco.pack()
        self.labelPreco = tkinter.Label(self.framePreco, text="Preco: ")
        self.labelPreco.pack(side="left")
        self.inputPreco = tkinter.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")

        self.frameButton = tkinter.Frame(self) 
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Cadastro")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastraPeixe)
    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewMostra(tkinter.Toplevel):
    def __init__(self, controle, lista ):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("")
        self.controle = controle 

        self.frameMostra = tkinter.Frame(self)
        self.frameMostra.pack()
        for peixe in lista:
            self.labelMostra = tkinter.Label(self.frameMostra, text=f"Nome: {peixe.nome}  Preco: {peixe.preco} ")
            self.labelMostra.pack()

class ViewCompra(tkinter.Toplevel):
    def __init__(self, controle, listaPeixes):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("")
        self.controle = controle 

        self.framePeixes = tkinter.Frame(self)
        self.framePeixes.pack()
        self.labelPeixesframePeixes = tkinter.Label(self.framePeixes, text="Escolha: ")
        self.labelPeixesframePeixes.pack(side="left")
        self.escolhaCombo = tkinter.StringVar()
        self.combobox = ttk.Combobox(self.framePeixes, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaPeixes

        self.framePeso = tkinter.Frame(self)
        self.framePeso.pack()
        self.labelPeso = tkinter.Label(self.framePeso, text="Peso: ")
        self.labelPeso.pack(side="left")
        self.inputPeso = tkinter.Entry(self.framePeso, width=20)
        self.inputPeso.pack(side="left")

        self.frameButton = tkinter.Frame(self) 
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Adiciona Peixe")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.addPeixe)

        self.frameButton = tkinter.Frame(self) 
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Fecha comaanda")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.geraComanda)

class ViewFaturamento(tkinter.Toplevel):
    def __init__(self, controle, msg):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("")
        self.controle = controle 

        self.frameMostra = tkinter.Frame(self)
        self.frameMostra.pack()
        self.labelMostra = tkinter.Label(self.frameMostra, text=f"FAturamento \n {msg}")
        self.labelMostra.pack()

class CtrlPeixe():
    def __init__(self, controlePrincipal):
        self.listaPeixes = []
        self.compras = []
        self.comandas= []
        self.ctrlPrincipal = controlePrincipal


    def cadastroPeixe(self):
        self.viewCadastraPeixe = ViewCadastro(self)

    def mostraPeixe(self):
        self.viewMostraPeixe = ViewMostra(self, self.listaPeixes)

    
    def cadastraPeixe(self, event):
        nome = self.viewCadastraPeixe.inputNomePeixe.get()
        preco = self.viewCadastraPeixe.inputPreco.get()
        peixe = Peixe(nome, preco)
        self.listaPeixes.append(peixe)

        self.viewCadastraPeixe.mostraJanela("Sucesso", "Peixe cadastrado")

    def compraPeixe(self):
        nomePeixe = []
        for peixe in self.listaPeixes:
            nomePeixe.append(peixe.nome)
        self.viewCompraPeixe = ViewCompra(self, nomePeixe)

    def addPeixe(self, event):
        peixe = self.viewCompraPeixe.escolhaCombo.get()
        peso = float(self.viewCompraPeixe.inputPeso.get())

        for peixes in self.listaPeixes:
            if peixes.nome == peixe:
                valorKG = float(peixes.preco)
                break

        valor = valorKG * peso

        itemComanda = ItemComanda(peixe, valor, peso)
        self.compras.append(itemComanda)

    def geraComanda(self, event):
        msg = ""
        valortt = 0
        for compra in self.compras:
            msg += f"Peixe: {compra.nome} - Peso: {compra.peso} - Valor: R${compra.preco}\n"
            valortt += float(compra.preco)

        msg += f"\n\nValor total as ser pago: R${valortt}"
        self.viewCadastraPeixe.mostraJanela("Comanda", msg)

        comanda = Comanda(self.compras)
        self.comandas.append(comanda)
        self.compras = []

    def faturamento(self):
        msg = ""
        for peixe in self.listaPeixes:
            vtt = 0
            ptt = 0
            for comanda in self.comandas:#  ja que comanda tem uma lista de itens  precisamos percorrela tbm
                for item in comanda.itens:
                    if peixe.nome == item.nome:
                        vtt += item.preco
                        ptt += item.peso
            msg += f"Peixe: {peixe.nome} - {ptt} Kg - {vtt}\n"

        self.view_faturamento = ViewFaturamento(self, msg)
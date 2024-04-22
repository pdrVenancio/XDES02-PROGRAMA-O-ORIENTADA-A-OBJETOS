import tkinter
from tkinter import messagebox
import pickle
import os.path


class Produto():
    def __init__(self, codigo, descricao, precoPerKg):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__precoPerKg = precoPerKg

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def precoPerKg(self):
        return self.__precoPerKg

    @precoPerKg.setter
    def precoPerKg(self, valor):
        self.__precoPerKg = valor


class ViewCadastroProduto(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("360x160")
        self.title("Cadastro")
        self.controle = controle

        self.frameCod = tkinter.Frame(self)
        self.frameDescricao = tkinter.Frame(self)
        self.framePreco = tkinter.Frame(self)
        self.frameCod.pack()
        self.frameDescricao.pack()
        self.framePreco.pack()
        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()

        self.labelCod = tkinter.Label(self.frameCod, text="Código: ")
        self.labelCod.pack(side="left")
        self.labelDescricao = tkinter.Label(self.frameDescricao,
                                            text="Descricao: ")
        self.labelDescricao.pack(side="left")
        self.labelPreco = tkinter.Label(self.framePreco, text="Preço por Kg: ")
        self.labelPreco.pack(side="left")

        self.inputCod = tkinter.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")
        self.inputDescricao = tkinter.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")
        self.inputPreco = tkinter.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")

        self.buttonSubmit = tkinter.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastrarProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ViewRemoveProduto(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("360x160")
        self.title("Remoção")
        self.controle = controle

        self.frameCod = tkinter.Frame(self)
        self.frameCod.pack()
        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()

        self.labelCod = tkinter.Label(self.frameCod, text="Código: ")
        self.labelCod.pack(side="left")
        self.inputCod = tkinter.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.buttonSubmit = tkinter.Button(self.frameButton, text="Remover")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.removerProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ViewAlteraProduto(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("360x160")
        self.title("Cadastro")
        self.controle = controle

        self.frameCod = tkinter.Frame(self)
        self.frameDescricao = tkinter.Frame(self)
        self.framePreco = tkinter.Frame(self)
        self.frameCod.pack()
        self.frameDescricao.pack()
        self.framePreco.pack()
        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()

        self.labelCod = tkinter.Label(self.frameCod, text="Código: ")
        self.labelCod.pack(side="left")
        self.labelDescricao = tkinter.Label(self.frameDescricao,
                                            text="Descrição: ")
        self.labelDescricao.pack(side="left")
        self.labelPreco = tkinter.Label(self.framePreco, text="Preço: ")
        self.labelPreco.pack(side="left")

        self.inputCod = tkinter.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")
        self.inputDescricao = tkinter.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left")
        self.inputPreco = tkinter.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")

        self.buttonSubmit = tkinter.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.alterarProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ViewConsultaProduto(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("360x160")
        self.title("Consulta")
        self.controle = controle

        self.frameCod = tkinter.Frame(self)
        self.frameCod.pack()
        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()

        self.labelCod = tkinter.Label(self.frameCod, text="Código: ")
        self.labelCod.pack(side="left")
        self.inputCod = tkinter.Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")

        self.buttonSubmit = tkinter.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultarProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlProduto():

    def __init__(self, controleprincipal):
        if not os.path.isfile("produtos.pickle"):
            self.listaProdutos = [
                Produto("1", "Linguiça", 25),
                Produto("2", "Toucinho", 14),
                Produto("3", "Lombo", 22),
                Produto("4", "Alcatra", 45),
                Produto("5", "Filé mignon", 60),
            ]
        else:
            with open("produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)
        self.controlePrincipal = controleprincipal

    def getListaProduto(self):
        return self.listaProdutos

    def cadastraProduto(self):
        self.viewCadastroProduto = ViewCadastroProduto(self)

    def removeProduto(self):
        self.viewRemoveProduto = ViewRemoveProduto(self)

    def alteraProduto(self):
        self.viewAlteraProduto = ViewAlteraProduto(self)

    def consultaProduto(self):
        self.viewConsultaProduto = ViewConsultaProduto(self)

    def cadastrarProduto(self, event):
        cod = self.viewCadastroProduto.inputCod.get()
        descricao = self.viewCadastroProduto.inputDescricao.get()
        preco = self.viewCadastroProduto.inputPreco.get()

        if len(cod) == 0 or len(descricao) == 0 or len(preco) == 0:
            self.viewCadastroProduto.mostraJanela("Erro","Preencha todos os campos!")
            return

        if not cod.isnumeric() or not preco.isnumeric():
            self.viewCadastroProduto.mostraJanela("Erro","Os campos cod e preco devem ser numericos!")
            return

        produto = Produto(cod, descricao, preco)
        self.listaProdutos.append(produto)

        self.viewCadastroProduto.mostraJanela(
            'Cadastro', 'Produto cadastrado com sucesso')
        self.viewCadastroProduto.destroy()

    def removerProduto(self, event):
        cod = self.viewRemoveProduto.inputCod.get()

        if len(cod) == 0:
            self.viewCadastroProduto.mostraJanela("Erro", "Preencha o campo vazio!")
            return

        for produto in self.listaProdutos:
            if produto.codigo == cod:
                self.listaProdutos.remove(produto)
                self.viewRemoveProduto.mostraJanela(
                    'Remover', 'Produto removido com sucesso')
                break
        else:
            self.viewRemoveProduto.mostraJanela(
                'Remover', 'Produto não pode ser removido')

    def alterarProduto(self, event):
        cod = self.viewAlteraProduto.inputCod.get()
        descricao = self.viewAlteraProduto.inputDescricao.get()
        preco = self.viewAlteraProduto.inputPreco.get()

        if len(cod) == 0 or len(descricao) == 0 or len(preco) == 0:
            self.viewCadastroProduto.mostraJanela("Erro","Preencha todos os campos!")
            return

        for produto in self.listaProdutos:
            if produto.codigo == cod:
                produto.descricao = descricao
                produto.precoPerKg = preco
                self.viewAlteraProduto.mostraJanela(
                    'Alterar', 'Produto alterado com sucesso')
                break
        else:
            self.viewAlteraProduto.mostraJanela('Erro','Produto não encontrado')

        self.viewAlteraProduto.destroy()

    def consultarProduto(self, event):
        cod = self.viewConsultaProduto.inputCod.get()
        msg = ""

        if len(cod) == 0:
            self.viewCadastroProduto.mostraJanela("Erro", "Preencha todos os campos!")
            return

        for prod in self.listaProdutos:
            if cod == prod.codigo:
                msg += f'Preço po kg: {prod.precoPerKg}\nDescrição: {prod.descricao}\n'
                break
        else:
            msg = "Produto não encontrado"

        self.viewConsultaProduto.mostraJanela('Consulta', msg)

    def returnListaProd(self):
        return self.listaProdutos

    def salvaProduto(self):
        if len(self.listaProdutos) != 0:
            with open("produtos.pickle", "wb") as f:
                pickle.dump(self.listaProdutos, f)

    def mostraProdutosCadastrados(self):
        self.viewProduto = ViewCadastroProduto(self)
        self.viewProduto.destroy()
        msg = "========================================================\n"
        msg = f"Número de produtos cadastrados: {len(self.listaProdutos)}\n\n\n"
        num = 1
        for prd in self.listaProdutos:
            msg += f"PRODUTO {prd.codigo}\n"
            msg += "Descrição: " + prd.descricao + "\n" + "Preço por KG: " + str(prd.precoPerKg) + "\n\n"
            num += 1

        messagebox.showinfo("Lista de produtos cadastrados", msg)
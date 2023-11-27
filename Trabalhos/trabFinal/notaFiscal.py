from sre_constants import CATEGORY_LOC_WORD
import tkinter
from tkinter import messagebox
from typing import Text
import cliente
from collections import Counter


class NotaFiscal():
    def __init__(self, numero, cliente, produtos, dataEmissao, valorTotal):
        self.__numero = numero 
        self.__cliente = cliente  
        self.__produtos = produtos  
        self.__dataEmissao = dataEmissao 
        self.__valorTotal = valorTotal

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
        self.buttonCpf = tkinter.Button(self.frameButton, text="Buscar")
        self.buttonCpf.pack(side="left")
        self.buttonCpf.bind("<Button>", controle.buscarCpf)
        self.buttonCancel = tkinter.Button(self.frameButton, text="Cancelar")
        self.buttonCancel.pack(side="left")
        self.buttonCancel.bind("<Button>", controle.cancelarBusca)

    def mostraSucesso(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def mostraErro(self, titulo, msg):
        messagebox.showerror(titulo, msg)

    def escolhaProd(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Cadsaçl´~as")
        self.controle = controle
        self.frameCompra = tkinter.Frame(self)
        self.frameCompra.pack()

        #produto
        self.labelProduto = tkinter.Label(self.frameCompra, text="Produto: ")
        self.labelProduto.pack()
        self.inputProduto = tkinter.Entry(self.frameCompra, width=20)
        self.inputProduto.pack()
        #quantidade
        self.labelQuantidade = tkinter.Label(self.frameCompra,
                                             text="Quantidade: ")
        self.labelQuantidade.pack()
        self.inputQuantidade = tkinter.Entry(self.frameCompra, width=20)
        self.inputQuantidade.pack()
        #data
        self.labelData = tkinter.Label(self.frameCompra,
                                       text="Data de compra: ")
        self.labelData.pack()
        self.inputData = tkinter.Entry(self.frameCompra, width=20)
        self.inputData.pack()

        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Comprar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.addProdNota)

        self.buttonGerar = tkinter.Button(self.frameButton, text="Emitir nota")
        self.buttonGerar.pack(side="left")
        self.buttonGerar.bind("<Button>", controle.gerarNota)


class ViewFaturamentoProduto(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Emitir nota Fiscal")
        self.controle = controle

        self.frameProduto = tkinter.Frame(self)
        self.frameProduto.pack()

        #produto
        self.labelProduto = tkinter.Label(self.frameProduto, text="Produto: ")
        self.labelProduto.pack()
        self.inputProduto = tkinter.Entry(self.frameProduto, width=20)
        self.inputProduto.pack()

        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.faturamentoProduto)


class ViewFaturamentoCliente(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Emitir nota Fiscal")
        self.controle = controle

        self.frameCliente = tkinter.Frame(self)
        self.frameCliente.pack()

        #produto
        self.labelCliente = tkinter.Label(self.frameCliente, text="Cliente: ")
        self.labelCliente.pack()
        self.inputCliente = tkinter.Entry(self.frameCliente, width=20)
        self.inputCliente.pack()

        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.faturamentoCliente)


class ViewFaturamentoPeriodo(tkinter.Toplevel):

    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Emitir nota Fiscal")
        self.controle = controle

        self.frameInicio = tkinter.Frame(self)
        self.frameInicio.pack()
        self.labelInicio = tkinter.Label(self.frameInicio, text="Inicio: ")
        self.labelInicio.pack()
        self.inputInicio = tkinter.Entry(self.frameInicio, width=20)
        self.inputInicio.pack()

        self.frameFinal = tkinter.Frame(self)
        self.frameFinal.pack()
        self.labelFinal = tkinter.Label(self.frameFinal, text="Final: ")
        self.labelFinal.pack()
        self.inputFinal = tkinter.Entry(self.frameFinal, width=20)
        self.inputFinal.pack()

        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.faturamentoPeriodo)

class ViewFaturamentoPeriodoCliente(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Emitir nota Fiscal")
        self.controle = controle

        self.frameCod = tkinter.Frame(self)
        self.frameCod.pack()
        self.labelCod = tkinter.Label(self.frameCod, text="Codigo do cliente: ")
        self.labelCod.pack()
        self.inputCod = tkinter.Entry(self.frameCod, width=20)
        self.inputCod.pack()

        self.frameInicio = tkinter.Frame(self)
        self.frameInicio.pack()
        self.labelInicio = tkinter.Label(self.frameInicio, text="Inicio: ")
        self.labelInicio.pack()
        self.inputInicio = tkinter.Entry(self.frameInicio, width=20)
        self.inputInicio.pack()

        self.frameFinal = tkinter.Frame(self)
        self.frameFinal.pack()
        self.labelFinal = tkinter.Label(self.frameFinal, text="Final: ")
        self.labelFinal.pack()
        self.inputFinal = tkinter.Entry(self.frameFinal, width=20)
        self.inputFinal.pack()

        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.faturamentoPeriodoCliente)

class ViewRankProdutos(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry("300x300")
        self.title("Produtos mais vendidos")
        self.controle = controle

        self.frameButton = tkinter.Frame(self)
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Consultar Produtos mais vendidos")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.produtosMaisvendidos)
  
class CtrlNotaFiscal():

    def __init__(self, controleprincipal):
        self.controlePrincipal = controleprincipal
        self.listaProdutos = controleprincipal.ctrlProduto.getListaProduto()  #pega a lista de todos os produtos registrados
        self.cpfCliente = ""
        self.listaCompra = []
        self.listaNota = []

    def emitirNota(self):
        self.viewEmitirNota = ViewEmitirNota(self)

    def buscarCpf(self, event):
        cpf = self.viewEmitirNota.inputCpf.get()
        if cpf == "":
            self.viewEmitirNota.mostraErro("Erro", "Digite um CPF")
        else:
            for c in cliente.CtrlCliente.listaClientes:
                if c.cpf == cpf:
                    self.viewEmitirNota.escolhaProd(self)
                    self.cpfCliente = cpf
                    break
            else:
                self.viewEmitirNota.mostraErro("Erro", "Cliente não encontrado!\nCadastre um cliente antes de prosseguir")
                return

    def cancelarBusca(self, event):
        self.viewEmitirNota.destroy()

    def addProdNota(self, event):
        produto = self.viewEmitirNota.inputProduto.get()
        quantidade = float(self.viewEmitirNota.inputQuantidade.get())
        self.valortt = 0
        preco = 0
        nome = ""
        cod = ""
        for prd in self.listaProdutos:
            if prd.codigo == produto:
                preco = prd.precoPerKg
                nome = prd.descricao
                cod = prd.codigo
                break
        else:
            self.viewEmitirNota.mostraErro("Erro", "Produto não encontrado")

        valor = float(quantidade) * float(preco)
        self.listaCompra.append((cod, nome, quantidade, valor))
        self.valortt += float(valor)
        print(self.valortt)
        msg = f"Produto: {cod}\nDescrição: {nome}\nValor: {valor}"
        self.viewEmitirNota.mostraSucesso("Produto adicionado com sucesso!", msg)

    def calculaNumNota(self):
        n = None
        for nota in self.listaNota:
            n = nota.numero

        if n is not None:
            n += 1
        else:
            n = 1
        return n

    def gerarNota(self, event):
        cpf = ""
        data = self.viewEmitirNota.inputData.get()
        for clt in cliente.CtrlCliente.listaClientes:
            if clt.cpf == self.cpfCliente:
                cpf = clt.cpf
        
        numero = self.calculaNumNota()

        nota = NotaFiscal(numero, cpf, self.listaCompra, data, self.valortt)
        self.listaNota.append(nota)

        msg = ""
        for nota in self.listaNota:
            msg += f"Número: {nota.numero}\nCPF: {nota.cliente}\nData: {nota.dataEmissao}\nValor total: {nota.valorTotal}\n"
        self.viewEmitirNota.mostraSucesso("Nota Fiscal gerada com sucesso!",msg)
        self.viewEmitirNota.destroy()

    def fatProduto(self):
        self.viewFaturamentoProduto = ViewFaturamentoProduto(self)

    def fatCliente(self):
        self.viewFaturamentoCliente = ViewFaturamentoCliente(self)

    def fatPeriodo(self):
        self.viewFaturamentoPeriodo = ViewFaturamentoPeriodo(self)

    def fatPeriodoCliente(self):
        self.viewFaturamentoPeriodoCliente = ViewFaturamentoPeriodoCliente(self)

    def faturamentoProduto(self, event):
        produtoProcurado = self.viewFaturamentoProduto.inputProduto.get()
        vtotalProduto = 0
        for nota in self.listaNota:
            for produto in nota.produtos:
                
                if produto[0] == produtoProcurado:
                    vtotalProduto += produto[3]
                break
                

        msg = f"Faturamento total do produto {produtoProcurado}: {vtotalProduto}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def faturamentoCliente(self, event):
        clienteProcurado = self.viewFaturamentoCliente.inputCliente.get()
        vtotalCliente = 0
        for nota in self.listaNota:
            if nota.cliente == clienteProcurado:
                vtotalCliente += nota.valorTotal

        msg = f"Faturamento total do cliente {clienteProcurado}: {vtotalCliente}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def faturamentoPeriodo(self, event):
        data1 = self.viewFaturamentoPeriodo.inputInicio.get()
        data2 = self.viewFaturamentoPeriodo.inputFinal.get()
        vtotal = 0
        for nota in self.listaNota:
            if nota.dataEmissao >= data1 and nota.dataEmissao <= data2:
                vtotal += nota.valorTotal

        msg = f"O faturamento do periodo de {data1} ate {data2} foi de {vtotal}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def faturamentoPeriodoCliente(self, event):
        clienteProcurado = self.viewFaturamentoPeriodoCliente.inputCod.get()
        data1 = self.viewFaturamentoPeriodoCliente.inputInicio.get()
        data2 = self.viewFaturamentoPeriodoCliente.inputFinal.get()
        msg = ""
        cont = 0
        for nota in self.listaNota:
            if nota.dataEmissao >= data1 and nota.dataEmissao <= data2 and nota.cliente == clienteProcurado:
                cont +=1
                msg += f"Valor da nota: {nota.valorTotal}\n"

        msg += f"\n\nTotal de notas Emitidas: {cont}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def rankProdutos(self):
        self.viewRankProdutos = ViewRankProdutos(self) 
#Preciso saber quis sao os 5 produtos mais vendidos
    def produtosMaisVendidos(self):
# Criar um dicionário para armazenar informações sobre os produtos
        info_produtos = {}
        
        # Iterar sobre todas as notas fiscais
        for nota in self.listaNota:
            for produto in nota.produtos:
                cod_produto = produto[0]
                descricao = ""
                preco_por_kg = 0
        
                # Procurar as informações do produto na lista de produtos
                for prd in self.listaProdutos:
                    if prd.codigo == cod_produto:
                        descricao = prd.descricao
                        preco_por_kg = prd.precoPerKg
                        break
        
                # Calcular o valor total obtido com a venda do produto
                valor_total = produto[2] * preco_por_kg
        
                # Atualizar as informações do produto no dicionário
                if cod_produto not in info_produtos:
                    info_produtos[cod_produto] = {
                        "descricao": descricao,
                        "preco_por_kg": preco_por_kg,
                        "quantidade_vendida": produto[2],
                        "valor_total": valor_total
                    }
                else:
                    info_produtos[cod_produto]["quantidade_vendida"] += produto[2]
                    info_produtos[cod_produto]["valor_total"] += valor_total
        
        # # info_produtos.items(): Transforma o dicionário info_produtos em uma lista de tuplas,
        # onde cada tupla contém um par chave-valor do dicionário. A função items() retorna uma visão de todos os 
        # itens no dicionário, e o sorted posterior ordenará essas tuplas.

        # # sorted(...): Ordena a lista de tuplas com base em um critério específico. 
        # O argumento key é uma função que especifica uma chave de classificação. Neste caso, é uma função lambda que extrai o valor 
        # associado à chave quantidade_vendida no segundo elemento da tupla (x[1]).

        # # reverse=True: Indica que a ordenação deve ser feita em ordem decrescente. 
        # Ou seja, os itens com a maior quantidade vendida aparecerão primeiro.

        # # [:5]: Realiza uma fatia na lista resultante, pegando apenas os primeiros cinco elementos. 
        # Isso garante que a lista produtos_mais_vendidos contenha apenas as informações dos cinco produtos mais vendidos.
        produtos_mais_vendidos = sorted(info_produtos.items(), key=lambda x: x[1]["quantidade_vendida"], reverse=True)[:5]# Ordenar a lista 
        

        msg = "Os 5 produtos mais vendidos:\n\n"
        p = 1
        for cod_produto, info in produtos_mais_vendidos:
            
            msg +=f"{p} posicao: \n Código: {cod_produto},\n Descrição: {info['descricao']}\n Preço por Kg: {info['preco_por_kg']}\n Quantidade Vendida: {info['quantidade_vendida']} kg \n Valor Total: R${info['valor_total']:.2f}\n\n"
            p+=1
        self.viewEmitirNota.mostraSucesso("Rank Produtos", msg)
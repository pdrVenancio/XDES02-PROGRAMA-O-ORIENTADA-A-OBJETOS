from datetime import  datetime
import tkinter
from tkinter import messagebox
import cliente
import pickle
import os.path



class NotaFiscal():
    def __init__(self, numero, cpfCliente, produtos, dataEmissao, valorTotal):
        self.__numero = numero 
        self.__cpfCliente = cpfCliente  
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
    def cpfCliente(self):
        return self.__cpfCliente

    @cpfCliente.setter
    def cpfCliente(self, valor):
        self.__cpfCliente = valor

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

    @property
    def getListaProd(self):
        msg = ''
        for produto in self.__produtos:
            msg += '\n\nProduto: ' + produto[1] + ' - ' + 'Quantidade: ' + str(produto[2])+'Kg' + '\n' + 'Valor: ' + 'R$' +str(produto[3])     
        return msg


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
        self.buttonCancel.bind("<Button>", controle.fecharJanela)

    def mostraSucesso(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def mostraErro(self, titulo, msg):
        messagebox.showerror(titulo, msg)

    def escolhaProd(self, controle, coletaNome):
        self.title("Emitir nota Fiscal")
        self.controle = controle
        self.frameNome = tkinter.Frame(self)
        self.frameNome.pack()
        self.frameCompra = tkinter.Frame(self)
        self.frameCompra.pack()

        #   Tirar o frame do CPF e dos BOTÕES para inserção dos produtos
        self.frameCpf.destroy()
        self.frameButton.destroy()

        # Aparecer o nome do cliente
        nomeCliente = coletaNome

        linhaSuperior = tkinter.Label(self.frameNome, text="=-" * 20)
        linhaSuperior.grid(row=0, column=0, columnspan=3)  # columnspan=3 garante que a linha cobre todas as colunas

        nomeCliente_label = tkinter.Label(self.frameNome, text=nomeCliente, fg="blue")
        nomeCliente_label.grid(row=1, column=1)

        linhaInferior = tkinter.Label(self.frameNome, text="=-" * 20)
        linhaInferior.grid(row=2, column=0, columnspan=3)  # columnspan=3 garante que a linha cobre todas as colunas



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

        self.buttonCancel = tkinter.Button(self.frameButton, text="Cancelar")
        self.buttonCancel.pack(side="left")
        self.buttonCancel.bind("<Button>", controle.fecharJanela)

class ViewExibirNota(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("400x200")
        self.title("Consultar nota")

        self.frameNumNota = tkinter.Frame(self)
        self.frameNumNota.pack()
        self.frameButtons = tkinter.Frame(self)
        self.frameButtons.pack()

        self.labelNum = tkinter.Label(self.frameNumNota, text="Informe o número da nota: ")
        self.labelNum.pack(side="left")
        self.inputNum = tkinter.Entry(self.frameNumNota)
        self.inputNum.pack(side="left")
        self.buttonConsultar = tkinter.Button(self.frameButtons, text="Consultar")
        self.buttonConsultar.pack(side="left")
        self.buttonConsultar.bind("<Button>", controle.botaoExibirNota)
        self.buttonCancelar = tkinter.Button(self.frameButtons, text="Cancelar")
        self.buttonCancelar.pack(side="left")
        self.buttonCancelar.bind("<Button>", controle.botaoCancelarConsulta)

    def mostraSucesso(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def mostraErro(self, titulo, msg):
        messagebox.showerror(titulo, msg)

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
        self.listaProdutos = controleprincipal.ctrlProduto.getListaProduto() 
        self.cpfCliente = ""
        self.listaCompra = []

        if not os.path.isfile("nota.pickle"):
            self.listaNota = []
        else:
            with open("nota.pickle", "rb") as f:
                self.listaNota = pickle.load(f)


    def emitirNota(self):
        self.viewEmitirNota = ViewEmitirNota(self)

    def exibirNota(self):
        self.viewExibirNota = ViewExibirNota(self)

    def buscarCpf(self, event):
        cpf = self.viewEmitirNota.inputCpf.get()
        if cpf == "":
            self.viewEmitirNota.mostraErro("Erro", "Digite um CPF")
        else:
            for c in cliente.CtrlCliente.listaClientes:
                if c.cpf == cpf:
                    self.viewEmitirNota.escolhaProd(self, coletaNome=c.nome)
                    self.cpfCliente = cpf
                    break
            else:
                self.viewEmitirNota.mostraErro("Erro", "Cliente não encontrado!\nCadastre um cliente antes de prosseguir")
                return

    def fecharJanela(self, event):
        self.viewEmitirNota.destroy()

    def addProdNota(self, event):
        if len(self.listaCompra) >= 10:
            self.viewEmitirNota.mostraErro("Erro", "Limite máximo de 10 produtos diferentes atingidos")
            return
        codigoProd = self.viewEmitirNota.inputProduto.get()
        quantidade = float(self.viewEmitirNota.inputQuantidade.get())
        # self.valortt = 0
        preco = 0
        nome = ""
        cod = ""

        for prd in self.listaProdutos:
            if prd.codigo == codigoProd:
                preco = prd.precoPerKg
                nome = prd.descricao
                cod = prd.codigo
                break
        else:
            self.viewEmitirNota.mostraErro("Erro", "Produto inexistente")
            return

        # Função que atualiza produto se já existente na lista de compras
        for prd in self.listaCompra:
            if prd[0] == codigoProd:
                prd[2] += quantidade
                prd[3] += float(preco) * quantidade
                self.viewEmitirNota.mostraSucesso("Sucesso", "Produto atualizado com sucesso")
                return

        valor = quantidade * float(preco)
        self.listaCompra.append([cod, nome, quantidade, valor])
        # self.valortt += float(valor)
        # print(self.valortt)
        msg = f"Descrição: {nome}\nValor: {valor}"
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
        valortt = 0
        data = self.viewEmitirNota.inputData.get()
        for clt in cliente.CtrlCliente.listaClientes:
            if clt.cpf == self.cpfCliente:
                cpf = clt.cpf

        if len(data) != 10 or data[2] != "/" or data[5] != "/":
            self.viewEmitirNota.mostraErro("Data inválida", "Data deve seguir o formato xx/xx/xxxx")
            return

        numero = self.calculaNumNota()

        for produto in self.listaCompra:
            valortt += produto[3]
            print(valortt)

        nota = NotaFiscal(numero, cpf, self.listaCompra, data, valortt)
        self.listaNota.append(nota)
        self.listaCompra = []

        msg = ""
        for nota in self.listaNota:
            msg = f"Número: {nota.numero}\nCPF: {nota.cpfCliente}\nData: {nota.dataEmissao}\nValor total: {nota.valorTotal}\n"
        self.viewEmitirNota.mostraSucesso("Nota Fiscal gerada com sucesso!",msg)
        self.viewEmitirNota.destroy()

    def botaoExibirNota(self, event):
        NumInserido = int(self.viewExibirNota.inputNum.get())
        msg = ""

        for nota in self.listaNota:
            if nota.numero == NumInserido:
                # Crie uma janela temporária para exibir a nota
                janelaTemporaria = tkinter.Toplevel()
                janelaTemporaria.geometry("365x350")
                janelaTemporaria.title(f"Nota {nota.numero}")
                janelaTemporaria.resizable(False, False)

                # Crie um Text widget na janela temporária
                textbox = tkinter.Text(janelaTemporaria, wrap="word", height=40, width=45)
                textbox.pack()

                msg = f"CPF do cliente: {nota.cpfCliente}\n"\
                    f"Nome do cliente: {cliente.CtrlCliente.getNome(nota.cpfCliente)}\n\n"\
                    + ("=" * 45) + "\n"\
                    f"LISTA DE PRODUTOS: {nota.getListaProd}\n"\
                    + ("=" * 45) + "\n"\
                    f"Valor total: R${nota.valorTotal}"

                textbox.insert("end", msg)

                scrollbar = tkinter.Scrollbar(janelaTemporaria, command=textbox.yview)
                scrollbar.pack(side="right", fill="y")

                textbox.config(yscrollcommand=scrollbar.set)

                break
        else:
            self.viewExibirNota.mostraErro("Erro", "Essa nota não existe!!")


    def botaoCancelarConsulta(self, event):
        self.viewExibirNota.destroy()

    def fatProduto(self):
        self.viewFaturamentoProduto = ViewFaturamentoProduto(self)

    def fatCliente(self):
        self.viewFaturamentoCliente = ViewFaturamentoCliente(self)

    def fatPeriodo(self):
        self.viewFaturamentoPeriodo = ViewFaturamentoPeriodo(self)

    def fatPeriodoCliente(self):
        self.viewFaturamentoPeriodoCliente = ViewFaturamentoPeriodoCliente(self)

    #Essa função só cria o view para que os faturamentos possam ser aplicados diretamente ao abrir o programa
    def criaView_Auxiliar(self):
        self.viewEmitirNota = ViewEmitirNota(self)
        self.viewEmitirNota.destroy()

    def validaData(self, data1, data2):
        if (len(data1) != 10 or (data1[2] != "/" or data1[5] != "/")) or (len(data2) != 10 or (data2[2] != "/" or data2[5] != "/")):
            self.viewEmitirNota.mostraErro("Datas inválidas", "As datas devem ser no formato xx/xx/xxxx")
            return 0

    def faturamentoProduto(self, event):
        self.criaView_Auxiliar()
        produtoProcurado = self.viewFaturamentoProduto.inputProduto.get()
        vtotalProduto = 0
        for nota in self.listaNota:
            for produto in nota.produtos:
                if produto[0] == produtoProcurado:
                    vtotalProduto += produto[3]

        msg = f"Faturamento total do produto {produtoProcurado}: {vtotalProduto}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def faturamentoCliente(self, event):
        self.criaView_Auxiliar()
        clienteProcurado = self.viewFaturamentoCliente.inputCliente.get()
        vtotalCliente = 0
        for nota in self.listaNota:
            if nota.cpfCliente == clienteProcurado:
                vtotalCliente += nota.valorTotal

        msg = f"Faturamento total do cliente {clienteProcurado}: {vtotalCliente}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def faturamentoPeriodo(self, event):
        self.criaView_Auxiliar()
        data1 = self.viewFaturamentoPeriodo.inputInicio.get()
        data2 = self.viewFaturamentoPeriodo.inputFinal.get()

        if self.validaData(data1, data2) == 0:
            return

        try:
            d1 = datetime.strptime(data1, '%d/%m/%Y')
            d2 = datetime.strptime(data2, '%d/%m/%Y')
        except ValueError as error:
            self.viewEmitirNota.mostraErro(error, "As datas são inválidas")

        vtotal = 0
        for nota in self.listaNota:
            notaData = datetime.strptime(nota.dataEmissao, '%d/%m/%Y')
            if notaData >= d1 and notaData <= d2:
                vtotal += nota.valorTotal

        msg = f"O faturamento do periodo de {data1} ate {data2} foi de {vtotal}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def faturamentoPeriodoCliente(self, event):
        self.criaView_Auxiliar()
        clienteProcurado = self.viewFaturamentoPeriodoCliente.inputCod.get()
        data1 = self.viewFaturamentoPeriodoCliente.inputInicio.get()
        data2 = self.viewFaturamentoPeriodoCliente.inputFinal.get()

        if self.validaData(data1, data2) == 0:
            return

        try:
            d1 = datetime.strptime(data1, '%d/%m/%Y')
            d2 = datetime.strptime(data2, '%d/%m/%Y')
        except ValueError as error:
            self.viewEmitirNota.mostraErro(error, "As datas devem ser no formato xx/xx/xxxx e devem ser numéricas")


        msg = ""
        cont = 0
        for nota in self.listaNota:
            notaData = datetime.strptime(nota.dataEmissao, '%d/%m/%Y')
            if notaData >= d1 and notaData <= d2 and nota.cpfCliente == clienteProcurado:
                cont +=1
                msg += f"Valor da nota: {nota.valorTotal}\n"

        msg += f"\n\nTotal de notas Emitidas: {cont}"
        self.viewEmitirNota.mostraSucesso("Faturamento",msg)

    def rankProdutos(self):
        self.viewRankProdutos = ViewRankProdutos(self) 

    def produtosMaisVendidos(self):
        self.criaView_Auxiliar()
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

    def salvaNota(self):
        if len(self.listaNota) != 0:
            with open("nota.pickle","wb") as f:
                pickle.dump(self.listaNota, f)

    def exibirNotasEmitidas(self):
        janelaTemporaria = tkinter.Toplevel()
        janelaTemporaria.geometry("365x500")
        janelaTemporaria.title("Notas Emitidas")
        janelaTemporaria.resizable(False, False)

        # Criar um Text widget na janela temporária
        textbox = tkinter.Text(janelaTemporaria, wrap="word", height=40, width=45)
        textbox.pack()

        msg = f"\tNúmero de notas emitidas: {len(self.listaNota)}\n\n\n"
        msg += ("=" * 45) + "\n\n"
        for nota in self.listaNota:
            msg += f"NOTA {nota.numero}\n"
            msg += f"Cliente: {cliente.CtrlCliente.getNome(nota.cpfCliente)} \n"
            msg += nota.getListaProd + "\n\n"
            msg += f"Data de Emissao: {nota.dataEmissao} \n"
            msg += f"Valor total: R${nota.valorTotal} \n\n"
            msg += ("=" * 45) + "\n\n\n"

        textbox.insert("end", msg)

        scrollbar = tkinter.Scrollbar(janelaTemporaria, command=textbox.yview)
        scrollbar.pack(side="right", fill="y")

        textbox.config(yscrollcommand=scrollbar.set)
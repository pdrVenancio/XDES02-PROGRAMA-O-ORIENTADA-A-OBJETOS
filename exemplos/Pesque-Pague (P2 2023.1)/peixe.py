import tkinter as tk
from tkinter import messagebox  #Função para mostrar uma janela de aviso
from tkinter import ttk         #Função para criar uma combobox

class Peixe:    #classe peixe
    def __init__(self, nome, preco):    #Construtor da classe Peixe
        self.__nome = nome
        self.__preco = preco

    #Getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    def getPeixe(self):
        return f"{self.__nome} - R${self.__preco:.2f}"  #retorna o nome e o preço do peixe
    
class PeixeComanda: #classe adicional para melhor controle dos peixes na comanda
    def __init__(self, Peixe, peso):    #Construtor da classe PeixeComanda
        self.__Peixe = Peixe
        self.__peso = peso

    #Getters
    @property
    def Peixe(self):
        return self.__Peixe
    
    @property
    def peso(self):
        return self.__peso
    
    def getPeixeComanda(self):
        return f"{self.__Peixe.nome} - {self.__peso:.3f} kg"    #retorna o nome e o peso do peixe
    
class Comanda:
    def __init__(self, listaPeixeComanda):  #Construtor da classe Comanda
        self.__listaPeixeComanda = listaPeixeComanda

    #Getters
    @property
    def listaPeixeComanda(self):
        return self.__listaPeixeComanda
    
    def getComanda(self):   #Retorna a comanda
        total = 0

        ret = "Comanda: \n" #Inicializando a string que será retornada

        for peixeComanda in self.__listaPeixeComanda:   #percorre a lista de peixes da comanda peixe por peixe
            valor = peixeComanda.Peixe.preco * peixeComanda.peso    #calcula o valor cobrado pelo peixe
            total += valor                                          #soma o valor do peixe ao total
            ret += peixeComanda.getPeixeComanda() + f" - R${valor:.2f}\n"

        ret += f"Total: R${total:.2f}"
        
        return ret
    
class LimiteCadastrarPeixe(tk.Toplevel): #classe da tela de cadastro de peixe
    def __init__(self, controle):
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('250x100')        #Dimensões da janela
        self.title("Cadastrar Peixe")   #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.frameNome = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.frameNome.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelPreco = tk.Label(self.framePreco,text="Preço: ")
        self.labelNome.pack(side="left")    #Empacota o labelNome no frameNome
        self.labelPreco.pack(side="left")   #Empacota o labelPreco no framePreco  

        #Entries são usados para receber entradas de texto
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")    #Empacota o inputNome no frameNome
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")   #Empacota o inputPreco no framePreco

        #Buttons são usados para criar botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")       #Botão Enter
        self.buttonSubmit.pack(side="left")                                 #Empacota o botão no frameButton
        self.buttonSubmit.bind("<Button>", controle.enterHandler)           #Vincula o botão a função enterHandler

        self.buttonClear = tk.Button(self.frameButton, text="Clear")        #Botão Clear
        self.buttonClear.pack(side="left")                                  #Empacota o botão no frameButton
        self.buttonClear.bind("<Button>", controle.clearHandler)            #Vincula o botão a função clearHandler

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")    #Botão Concluído
        self.buttonFecha.pack(side="left")                                  #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaHandler)            #Vincula o botão a função fechaHandler

    def mostraJanela(self, titulo, msg):    #Função para mostrar uma janela de aviso
        messagebox.showinfo(titulo, msg)    #Mostra uma janela de aviso com o título e a mensagem passados como parâmetro

class LimiteConsultaPeixe(tk.Toplevel): #classe da tela de exibição da lista de peixes
    def __init__(self, controle, peixes):   #Construtor da classe LimiteConsultaPeixe
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('250x300')        #Dimensões da janela
        self.title("Consultar Peixes")  #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.framePeixe = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.framePeixe.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelPeixe = tk.Label(self.framePeixe,text="Lista de peixes:")
        self.labelPeixe.pack(side="top")   #Empacota o labelPeixe no framePeixe

        #Texts são usados para mostrar textos
        self.textPeixe = tk.Text(self.framePeixe, height=10, width=30)  #Cria um textPeixe com 25 linhas e 30 colunas
        self.textPeixe.pack(side="top")                                 #Empacota o textPeixe no framePeixe
        self.textPeixe.insert(tk.END, peixes)                           #Insere o texto com a lista de peixes no textPeixe

        #Buttons são usados para criar botões
        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")    #Botão Concluído
        self.buttonFecha.pack(side="left")                                  #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaHandler)            #Vincula o botão a função fechaHandler

class LimiteFechaComanda(tk.Toplevel): #classe da tela de fechamento da comanda
    def __init__(self, controle, peixes): #Construtor da classe LimiteFechaComanda
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('250x300')        #Dimensões da janela
        self.title("Fechar Comanda")    #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.framePeixe = tk.Frame(self)
        self.framePeso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.framePeixe.pack()
        self.framePeso.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelPeixe = tk.Label(self.framePeixe,text="Peixe: ")
        self.labelPeso = tk.Label(self.framePeso,text="Peso: ")
        self.labelPeixe.pack(side="left")   #Empacota o labelPeixe no framePeixe
        self.labelPeso.pack(side="left")    #Empacota o labelPeso no framePeso

        #ComboBoxes são usados para criar caixas de seleção
        self.escolhaPeixe = tk.StringVar()                                                  #Cria uma variável para armazenar a escolha do peixe
        self.comboboxPeixe = ttk.Combobox(self.framePeixe,              #Frame onde a combobox será empacotada
                                          width = 15,                   #Largura da combobox
                                          values = peixes,              #Valores da combobox
                                          textvariable = self.escolhaPeixe)    #Cria uma combobox com as opções da lista de peixes
        self.comboboxPeixe.pack(side="left")                                                #Empacota a combobox no framePeixe

        #Entries são usados para receber entradas de texto
        self.inputPeso = tk.Entry(self.framePeso, width=20)
        self.inputPeso.pack(side="left")    #Empacota o inputPeso no framePeso

        #Buttons são usados para criar botões
        self.buttonAdd = tk.Button(self.frameButton, text="Adiciona Peixe")         #Botão Adiciona Peixe
        self.buttonAdd.pack(side="left")                                            #Empacota o botão no frameButton
        self.buttonAdd.bind("<Button>", controle.adicionaPeixeHandler)              #Vincula o botão a função adicionaPeixeHandler

        self.buttonFecha = tk.Button(self.frameButton, text="Fecha Comanda")        #Botão Concluído
        self.buttonFecha.pack(side="left")                                          #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaComandaHandler)             #Vincula o botão a função fechaHandler

    def mostraJanela(self, titulo, msg):    #Função para mostrar uma janela de aviso
        messagebox.showinfo(titulo, msg)    #Mostra uma janela de aviso com o título e a mensagem passados como parâmetro

class LimiteRelatorio(tk.Toplevel): #classe da tela de exibição do relatório
    def __init__(self, controle, relatorio): #Construtor da classe LimiteRelatorio
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('250x500')        #Dimensões da janela
        self.title("Relatório")         #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.frameRelatorio = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.frameRelatorio.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelRelatorio = tk.Label(self.frameRelatorio,text="Relatório:")
        self.labelRelatorio.pack(side="top")   #Empacota o labelRelatorio no frameRelatorio

        #Texts são usados para mostrar textos
        self.textRelatorio = tk.Text(self.frameRelatorio, height=10, width=30)  #Cria um textRelatorio com 25 linhas e 30 colunas
        self.textRelatorio.pack(side="top")                                     #Empacota o textRelatorio no frameRelatorio
        self.textRelatorio.insert(tk.END, relatorio)                            #Insere o texto com o relatório no textRelatorio

        #Buttons são usados para criar botões
        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")        #Botão Concluído
        self.buttonFecha.pack(side="left")                                      #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaHandler)                #Vincula o botão a função fechaHandler

class CtrlPeixe():  #classe de controle de peixe
    def __init__(self, controlePrincipal):  #Construtor da classe CtrlPeixe
        self.ctrlPrincipal = controlePrincipal    #Controle principal

        #Criação de uma lista de peixes
        self.listaPeixes = []

        #Criação de uma lista de peixes da comanda
        self.listaPeixesComanda = []    #essa lista é usada para armazenar os peixes adicionados a comanda

        #Criação de uma lista de comandas
        self.listaComandas = []

    def cadastrarPeixe(self):   #Função para cadastrar um peixe
        self.limite = LimiteCadastrarPeixe(self)    #Cria a tela de cadastro de peixe

    def enterHandler(self, event):  #Função para adicionar um peixe a lista de peixes
        nome = self.limite.inputNome.get()  #Recebe o nome do peixe
        preco = float(self.limite.inputPreco.get())    #Recebe o preço do peixe

        Px = Peixe(nome, preco) #Cria um objeto da classe Peixe

        self.listaPeixes.append(Px) #Adiciona o peixe a lista de peixes

        self.limite.mostraJanela('Sucesso', 'Peixe cadastrado com sucesso!')   #Mostra uma janela de aviso

        self.clearHandler(event)    #Chama a função clearHandler para limpar os campos de texto

    def clearHandler(self, event):  #Função para limpar os campos de texto
        self.limite.inputNome.delete(0, len(self.limite.inputNome.get()))  #Limpa o campo de texto do nome
        self.limite.inputPreco.delete(0, len(self.limite.inputPreco.get()))    #Limpa o campo de texto do preço

    def fechaHandler(self, event):  #Função para fechar a tela em exibição
        self.limite.destroy()   #Destroi a tela em exibição

    def consultarPeixe(self):   #Função para consultar os peixes cadastrados
        if len(self.listaPeixes) == 0:  #Verifica se a lista de peixes está vazia
            self.limite.mostraJanela('Erro', 'Não há peixes cadastrados!')   #Mostra uma janela de aviso
        else:
            peixes = ''

            for peixe in self.listaPeixes:  #Percorre a lista de peixes
                peixes += peixe.getPeixe() + "\n"   #Adiciona o peixe a string peixes

            self.limite = LimiteConsultaPeixe(self, peixes)    #Cria a tela de exibição da lista de peixes

    def gerarComanda(self):    #Função para gerar uma comanda
        if len(self.listaPeixes) == 0:  #Verifica se a lista de peixes está vazia
            self.limite.mostraJanela('Erro', 'Não há peixes cadastrados!')   #Mostra uma janela de aviso
        else:
            peixes = [] #Lista de nomes de peixes criados para serem usados no combobox

            for peixe in self.listaPeixes:  #Percorre a lista de peixes
                peixes.append(peixe.nome)   #Adiciona o nome do peixe a lista de peixes

            self.limite = LimiteFechaComanda(self, peixes)  #Cria a tela de fechamento da comanda

    def adicionaPeixeHandler(self, event):  #Função para adicionar um peixe a comanda
        nomPeixeEscolhido = self.limite.escolhaPeixe.get()   #Recebe o nome peixe escolhido
        peso = float(self.limite.inputPeso.get())   #Recebe o peso do peixe

        for peixe in self.listaPeixes:  #Percorre a lista de peixes
            if peixe.nome == nomPeixeEscolhido:   #Verifica se o nome do peixe é igual ao nome do peixe escolhido
                PeixeCmd = PeixeComanda(peixe, peso)    #Cria um objeto da classe PeixeComanda
                self.listaPeixesComanda.append(PeixeCmd)    #Adiciona o peixe a lista de peixes da comanda
                break

        self.limite.mostraJanela('Sucesso', 'Peixe adicionado com sucesso!')   #Mostra uma janela de aviso

        self.limite.escolhaPeixe.set('')    #Limpa o combobox de peixes
        self.limite.inputPeso.delete(0, len(self.limite.inputPeso.get()))  #Limpa o campo de texto do peso

    def fechaComandaHandler(self, event):   #Função para fechar a comanda
        if len(self.listaPeixesComanda) == 0:    #Verifica se a lista de peixes da comanda está vazia
            self.limite.mostraJanela('Erro', 'Não há peixes na comanda!')   #Mostra uma janela de aviso
        else:
            Com = Comanda(self.listaPeixesComanda)  #Cria um objeto da classe Comanda
            self.listaComandas.append(Com)  #Adiciona a comanda a lista de comandas
            self.listaPeixesComanda = []    #Limpa a lista de peixes da comanda

            self.limite.mostraJanela('Sucesso', 'Comanda fechada com sucesso!\nResumo:\n' + Com.getComanda())   #Mostra uma janela de aviso com o resumo da comanda

            self.limite.escolhaPeixe.set('')    #Limpa o combobox de peixes
            self.limite.inputPeso.delete(0, len(self.limite.inputPeso.get()))  #Limpa o campo de texto do peso

    def gerarRelatorio(self):   #Função para gerar um relatório
        if len(self.listaComandas) == 0:    #Verifica se a lista de comandas está vazia
            self.limite.mostraJanela('Erro', 'Não há comandas fechadas!')   #Mostra uma janela de aviso
        else:
            relatorio = ''
            faturamentoTotal = 0

            for peixe in self.listaPeixes:  #Percorre a lista de peixes
                valorTotalPeixe = 0
                pesoTotalPeixe = 0

                for comanda in self.listaComandas:  #Percorre a lista de comandas
                    for peixeComanda in comanda.listaPeixeComanda:  #Percorre a lista de peixes da comanda
                        if peixeComanda.Peixe.nome == peixe.nome:   #Verifica se o nome do peixe é igual ao nome do peixe da comanda
                            valorTotalPeixe += peixeComanda.Peixe.preco * peixeComanda.peso   #Adicona ao valor total do peixe
                            pesoTotalPeixe += peixeComanda.peso   #Adiciona ao peso total do peixe

                relatorio += f"{peixe.nome} - {pesoTotalPeixe:.3f} kg - R${valorTotalPeixe:.2f}\n"  #Adiciona o nome do peixe e o total a string relatorio
                faturamentoTotal += valorTotalPeixe #Adiciona o valor total do peixe ao faturamento total

            relatorio += f"Faturamento total: R${faturamentoTotal:.2f}" #Adiciona o faturamento total a string relatorio

            self.limite = LimiteRelatorio(self, relatorio)  #Cria a tela de exibição do relatório
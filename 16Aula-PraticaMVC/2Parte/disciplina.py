
# Aqui chamamos alguns amigos que vão nos ajudar a criar janelas e botões bonitinhos.
import tkinter as tk
from tkinter import messagebox

# Aqui criamos uma classe chamada "Disciplina", que guarda informações sobre uma disciplina, como código e nome.
class Disciplina:

    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    # Aqui criamos uns amigos especiais que ajudam a ver as informações da disciplina.
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome

# Agora, vamos criar uma janelinha para inserir disciplinas.
class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        # Aqui criamos algumas partes da janelinha, como rótulos (labels), caixas de texto e botões.
        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        # Rótulos
        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")

        # Caixas de texto
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    # Uma função para mostrar mensagens na tela.
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

# Agora, uma janelinha para mostrar a lista de disciplinas.
class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)

# Agora, uma classe que controla tudo relacionado às disciplinas.
class CtrlDisciplina():       
    def __init__(self):
        # Criamos uma lista de disciplinas com informações iniciais.
        self.listaDisciplinas = [
            Disciplina('COM220', 'Programação OO'),
            Disciplina('COM222', 'Programação Web'),
            Disciplina('COM111', 'Estruturas de Dados')
        ]

    # Função para pegar a lista de disciplinas.
    def getListaDisciplinas(self):
        return self.listaDisciplinas

    # Função para pegar uma disciplina com base no código.
    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.codigo == codDisc:
                discRet = disc
        return discRet

    # Função para pegar uma lista com os códigos de todas as disciplinas.
    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.codigo)
        return listaCod

    # Função para abrir a janelinha de inserção de disciplinas.
    def insereDisciplinas(self):
        self.limiteIns = LimiteInsereDisciplinas(self) 

    # Função para mostrar a lista de disciplinas em uma janelinha.
    def mostraDisciplinas(self):
        str = 'Código -- Nome\n'
        for disc in self.listaDisciplinas:
            str += disc.codigo + ' -- ' + disc.nome + '\n'
        self.limiteLista = LimiteMostraDisciplinas(str)

    # Função chamada quando o botão "Enter" é pressionado.
    def enterHandler(self, event):
        codDisc = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        disciplina = Disciplina(codDisc, nome)
        self.listaDisciplinas.append(disciplina)
        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
        self.clearHandler(event)

    # Função chamada quando o botão "Clear" é pressionado.
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    # Função chamada quando o botão "Concluído" é pressionado.
    def fechaHandler(self, event):
        self.limiteIns.destroy()

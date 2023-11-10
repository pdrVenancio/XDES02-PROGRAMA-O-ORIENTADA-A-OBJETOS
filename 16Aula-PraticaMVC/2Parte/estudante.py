
# Aqui estamos chamando alguns amigos que vão nos ajudar a criar janelas e botões bonitinhos.
import tkinter as tk
from tkinter import messagebox

# Aqui criamos uma classe chamada "Estudante", que guarda informações sobre um estudante, como número de matrícula e nome.
class Estudante:
    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome

    # Aqui criamos uns amigos especiais que ajudam a ver as informações do estudante.
    @property
    def nroMatric(self):
        return self.__nroMatric

    @property
    def nome(self):
        return self.__nome

# Agora, vamos criar uma janelinha para inserir estudantes.
class LimiteInsereEstudantes(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Estudante")
        self.controle = controle

        # Aqui criamos algumas partes da janelinha, como rótulos (labels), caixas de texto e botões.
        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        # Rótulos
        self.labelNro = tk.Label(self.frameNro, text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")

        # Caixas de texto
        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
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

# Agora, uma janelinha para mostrar a lista de estudantes.
class LimiteMostraEstudantes():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

# Agora, uma classe que controla tudo relacionado aos estudantes.
class CtrlEstudante():
    def __init__(self):
        # Criamos uma lista de estudantes com informações iniciais.
        self.listaEstudantes = [
            Estudante('1001', 'Joao Santos'),
            Estudante('1002', 'Marina Cintra'),
            Estudante('1003', 'Felipe Reis'),
            Estudante('1004', 'Ana Souza')
        ]

    # Função para pegar as informações de um estudante com base no número de matrícula.
    def getEstudante(self, nroMatric):
        estRet = None
        for est in self.listaEstudantes:
            if est.nroMatric == nroMatric:
                estRet = est
        return estRet

    # Função para pegar uma lista com os números de matrícula de todos os estudantes.
    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaEstudantes:
            listaNro.append(est.nroMatric)
        return listaNro

    # Função para abrir a janelinha de inserção de estudantes.
    def insereEstudantes(self):
        self.limiteIns = LimiteInsereEstudantes(self)

    # Função para mostrar a lista de estudantes em uma janelinha.
    def mostraEstudantes(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaEstudantes:
            str += est.nroMatric + ' -- ' + est.nome + '\n'
        self.limiteLista = LimiteMostraEstudantes(str)

    # Função chamada quando o botão "Enter" é pressionado.
    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        estudante = Estudante(nroMatric, nome)
        self.listaEstudantes.append(estudante)
        self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.clearHandler(event)

    # Função chamada quando o botão "Clear" é pressionado.
    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    # Função chamada quando o botão "Concluído" é pressionado.
    def fechaHandler(self, event):
        self.limiteIns.destroy()

# Olá amiguinho! Agora temos um código que ajuda a criar turmas de estudantes para disciplinas diferentes usando janelas e botões bonitinhos.

# Aqui chamamos alguns amigos que vão nos ajudar a criar janelas e botões bonitinhos.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Aqui criamos uma classe chamada "Turma", que guarda informações sobre uma turma, como código, disciplina e estudantes.
class Turma:

    def __init__(self, codigo, disciplina, estudantes):
        self.__codigo = codigo
        self.__disciplina = disciplina
        self.__estudantes = estudantes

    # Aqui criamos uns amigos especiais que ajudam a ver as informações da turma.
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def disciplina(self):
        return self.__disciplina

    @property
    def estudantes(self):
        return self.__estudantes

# Agora, vamos criar uma janelinha para inserir turmas.
class LimiteInsereTurma(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):
        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Turma")
        self.controle = controle

        # Aqui criamos algumas partes da janelinha, como rótulos (labels), caixas de texto, combobox e botões.
        self.frameCodTurma = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodTurma.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()

        # Rótulos e caixas de texto
        self.labelCodTurma = tk.Label(self.frameCodTurma, text="Informe o código da turma: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        # Rótulos e combobox
        self.labelDiscip = tk.Label(self.frameDiscip, text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip

        # Rótulos, listbox e botões
        self.labelEst = tk.Label(self.frameEstudante, text="Escolha o estudante: ")
        self.labelEst.pack(side="left")
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton, text="Insere Aluno")
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton, text="Cria Turma")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma)

    # Uma função para mostrar mensagens na tela.
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

# Agora, uma janelinha para mostrar a lista de turmas.
class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)

# Agora, uma classe que controla tudo relacionado às turmas.
class CtrlTurma():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaTurmas = []

    # Função para abrir a janelinha de inserção de turmas.
    def insereTurmas(self):        
        self.listaAlunosTurma = []
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric()
        self.limiteIns = LimiteInsereTurma(self, listaCodDisc, listaNroMatric)

    # Função para criar uma turma quando o botão "Cria Turma" é pressionado.
    def criaTurma(self, event):
        codTurma = self.limiteIns.inputCodTurma.get()
        discSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
        turma = Turma(codTurma, disc, self.listaAlunosTurma)
        self.listaTurmas.append(turma)
        self.limiteIns.mostraJanela('Sucesso', 'Turma criada com sucesso')
        self.limiteIns.destroy()

    # Função para inserir um aluno em uma turma quando o botão "Insere Aluno" é pressionado.
    def insereAluno(self, event):
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
        self.listaAlunosTurma.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE)

    # Função para mostrar a lista de turmas.
    def mostraTurmas(self):
        strTurmas = "Lista de Turmas:\n"
        for turma in self.listaTurmas:
            strTurmas += f"Código: {turma.codigo} | Disciplina: {turma.disciplina.nome} | Estudantes: {', '.join([est.nome for est in turma.estudantes])}\n"
        LimiteMostraTurmas(strTurmas)
    

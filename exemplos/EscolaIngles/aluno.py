from datetime import timedelta, datetime
from tkinter import messagebox, ttk
import tkinter

class Aluno():
    def __init__(self, nome: str, cpf :str, dNascimento, curso, nMatricula) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__dNascimento = dNascimento
        self.curso = curso
        self.__nMatricula = nMatricula

    @property
    def nome(self):
        return self.__nome
    
    @property
    def nMatricula(self):
        return self.__nMatricula
    
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def curso(self):
        return self.__curso
    
    @property
    def dNascimento(self):
        return self.__dNascimento
    
    @curso.setter
    def curso(self, valor):
        # Aqui estamos criando uma lista de cursos para crianças e outra para cursos regulares.
        self.cursosKids = ["K1","K2","K3","K4","K5","K6"]
        self.cursosReg = ["R1","R2","R3","R4","R5","R6","R7","R8"]

        # Vamos verificar se o curso que a pessoa escolheu está em uma das nossas listas.
        if not valor in self.cursosKids and not valor in self.cursosReg:
            # Se o curso não estiver em nenhuma das listas, vamos dizer que a escolha é inválida.
            raise ValueError("Escolha inválida: {}".format(valor))

        # Agora, estamos olhando para a data de nascimento da pessoa e vendo se ela tem pelo menos 13 anos.
        # Aqui estamos pegando a data de nascimento da pessoa e transformando em algo que o computador entenda assim podemos usala para calculos no futuro.
        dataNasc = datetime.strptime(self.__dNascimento, '%d/%m/%Y')

        # Agora, estamos calculando quanto tempo temos que adicionar à data de nascimento para chegar a 13 anos depois.
        trezeAnos = timedelta(days=365.2425*13)

        # Juntamos a data de nascimento com o tempo que calculamos para obter uma nova data, que representa 13 anos depois do nascimento.
        dataTeste = dataNasc + trezeAnos

        # Se a pessoa escolheu um curso regular, vamos verificar se ela tem mais de 13 anos.
        if dataTeste > datetime.now() and valor in self.cursosReg:
            # Se sim, mas ela tem menos de 13 anos, vamos dizer que a idade dela não é compatível com cursos regulares.
            raise ValueError("Idade incompatível com cursos Regulares")

        # Se a pessoa escolheu um curso para crianças, vamos verificar se ela tem menos de 13 anos.
        elif dataTeste < datetime.now() and valor in self.cursosKids:
            # Se sim, mas ela tem mais de 13 anos, vamos dizer que a idade dela não é compatível com cursos para crianças.
            raise ValueError("Idade incompatível com cursos Kids")

        # Se a escolha é válida e a idade está correta, vamos definir o curso escolhido.
        else:
            self.__curso = valor

    @property
    def getAluno(self):
        return f"Nome: {self.nome} \nNumero da matricula: {self.nMatricula}\nCpf: {self.cpf}\nCurso: {self.curso}\nData de nascimento: {self.dNascimento}"

class ViewCadastro(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("fdsfdsf")
        self.controle = controle        

        self.frameNome = tkinter.Frame(self)
        self.frameNome.pack()
        self.labelNome = tkinter.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tkinter.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.frameCPF = tkinter.Frame(self)
        self.frameCPF.pack()
        self.labelCPF = tkinter.Label(self.frameCPF, text="CPF: ")
        self.labelCPF.pack(side="left")
        self.inputCPF = tkinter.Entry(self.frameCPF, width=20)
        self.inputCPF.pack(side="left")

        self.frameCurso = tkinter.Frame(self)
        self.frameCurso.pack()
        self.labelCurso = tkinter.Label(self.frameCurso, text="Curso: ")
        self.labelCurso.pack(side="left")
        self.inputCurso = tkinter.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")

        self.frameDataNascimento = tkinter.Frame(self)
        self.frameDataNascimento.pack()
        self.labelDataNascimento = tkinter.Label(self.frameDataNascimento, text="Data nascimento: ")
        self.labelDataNascimento.pack(side="left")
        self.inputDataNascimento = tkinter.Entry(self.frameDataNascimento, width=20)
        self.inputDataNascimento.pack(side="left")


        self.frameNMatricula = tkinter.Frame(self)
        self.frameNMatricula.pack()
        self.labelNMatricula = tkinter.Label(self.frameNMatricula, text="NumeroMatricula: ")
        self.labelNMatricula.pack(side="left")
        self.inputNMatricula = tkinter.Entry(self.frameNMatricula, width=20)
        self.inputNMatricula.pack(side="left")

        self.frameButton = tkinter.Frame(self) 
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastrarAluno)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewConsulta(tkinter.Toplevel):
    def __init__(self, controle, listaKids, listaRegular):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("fdsfdsf")
        self.ctrl = controle   

        self.frameCombos = tkinter.Frame(self)
        self.frameCombos.pack(pady=3)

        self.labelKids = tkinter.Label(self.frameCombos,text="Kids: ")
        self.labelKids.pack(side="left")
        self.escolhaKids = tkinter.StringVar()
        self.comboboxKids = ttk.Combobox(self.frameCombos, width = 15 ,values=listaKids, textvariable = self.escolhaKids)
        self.comboboxKids.pack(side="left")
        self.comboboxKids.bind("<<ComboboxSelected>>", self.ctrl.exibeKids)

        self.labelRegular = tkinter.Label(self.frameCombos,text="Regulars: ")
        self.labelRegular.pack(side="left")
        self.escolhaRegular = tkinter.StringVar()
        self.comboboxRegular = ttk.Combobox(self.frameCombos, width = 15 ,values=listaRegular, textvariable = self.escolhaRegular)
        self.comboboxRegular.pack(side="left")
        self.comboboxRegular.bind("<<ComboboxSelected>>", self.ctrl.exibeRegular)

        self.frameInformacao = tkinter.Frame(self)
        self.frameInformacao.pack()
        self.textInformacao = tkinter.Text(self.frameInformacao, height=20,width=40)
        self.textInformacao.pack()
        self.textInformacao.config(state=tkinter.DISABLED)

class CtrlAluno():
    def __init__(self, controlePrincipal):
        self.listaAluno = []
        self.ctrlPrincipal = controlePrincipal

    def cadastroAluno(self):
        self.viewCadastro = ViewCadastro(self)

    def cadastrarAluno(self, event):
        nome = self.viewCadastro.inputNome.get()
        cpf = self.viewCadastro.inputCPF.get()
        nMat = self.viewCadastro.inputNMatricula.get()
        dNas = self.viewCadastro.inputDataNascimento.get()
        curso = self.viewCadastro.inputCurso.get()

        try:
            aluno = Aluno(nome, cpf, dNas, curso, nMat)
            self.listaAluno.append(aluno)
            self.viewCadastro.mostraJanela('Sucesso', 'Aluno cadastrado com sucesso')  # Correcao aqui
        except ValueError as error:
            self.viewCadastro.mostraJanela('Erro', error)  # Correcao aqui

    def consultaAluno(self):
        self.cursosKids = ["K1","K2","K3","K4","K5","K6"]
        self.cursosReg = ["R1","R2","R3","R4","R5","R6","R7","R8"] 
        self.cursosK = []
        self.cursosR = []       
        for aluno in self.listaAluno:
            if aluno.curso in self.cursosKids and aluno.curso not in self.cursosK:
                self.cursosK.append(aluno.curso)
            elif aluno.curso in self.cursosReg and aluno.curso not in self.cursosR:
                self.cursosR.append(aluno.curso)
        self.viewConsulta = ViewConsulta(self, self.cursosK,self.cursosR )

 
    def exibeKids(self, event):
        self.viewConsulta.comboboxRegular.set('---')

        kidsSel = self.viewConsulta.escolhaKids.get()

        self.viewConsulta.textInformacao.config(state='normal')
        self.viewConsulta.textInformacao.delete("1.0", tkinter.END)

        for aluno in self.listaAluno:
            if aluno.curso == kidsSel:
                kidsSel = f"{aluno.getAluno} \n\n"
                self.viewConsulta.textInformacao.insert(1.0, kidsSel)
        self.viewConsulta.textInformacao.config(state="disabled")

    def exibeRegular(self, event):
        self.viewConsulta.comboboxKids.set('---')

        regularSel = self.viewConsulta.comboboxRegular.get()

        self.viewConsulta.textInformacao.config(state='normal')
        self.viewConsulta.textInformacao.delete("1.0", tkinter.END)

        for aluno in self.listaAluno:
            if aluno.curso == regularSel:
                regularSel = f"{aluno.getAluno} \n\n"
                self.viewConsulta.textInformacao.insert(1.0, regularSel)
        self.viewConsulta.textInformacao.config(state="disabled")




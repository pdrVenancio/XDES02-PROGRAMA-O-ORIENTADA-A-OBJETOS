import tkinter
from tkinter import ttk, messagebox
import pickle
import os.path

class Equipe():
    def __init__(self, jogadores, nome) -> None:
        self.__nome = nome
        self.__jogadores = jogadores

    @property
    def jogadores(self):
        return self.__jogadores
    
    @property
    def nome(self):
        return self.__nome

class ViewCadastraEquipe(tkinter.Toplevel):
    def __init__(self, controle, listaNomeCurso):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("Cadastro de Equipes")
        self.controle = controle

        # Combobox com nome dos cursos
        self.frameCurso = tkinter.Frame(self)
        self.frameCurso.pack()
        self.labelCursoframeCurso = tkinter.Label(self.frameCurso, text="Escolha o curso: ")
        self.labelCursoframeCurso.pack(side="left")
        self.escolhaCombo = tkinter.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomeCurso

        # Digitar o numedo de matricula dos alunos
        self.frameNroMatricula = tkinter.Frame(self)
        self.frameNroMatricula.pack()
        self.labelNroMatricula = tkinter.Label(self.frameNroMatricula, text="NroMatricula: ")
        self.labelNroMatricula.pack(side="left")
        self.inputNroMatricula = tkinter.Entry(self.frameNroMatricula, width=20)
        self.inputNroMatricula.pack(side="left")
        
        # botao para verificar se o numero de matricula esta presente no curso
        self.frameButton = tkinter.Frame(self) 
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Cadastrar Aluno")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastraAluno)

        # botao para criar a equipe
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Criar equipe")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.criaEquipe)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewConsultaEquipe(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("Consulta de Equipes")
        self.controle = controle

        #sigla do curso 
        self.frameSigla = tkinter.Frame(self)
        self.frameSigla.pack()
        self.labelSigla = tkinter.Label(self.frameSigla, text="Sigla: ")
        self.labelSigla.pack(side="left")
        self.inputSigla = tkinter.Entry(self.frameSigla, width=20)
        self.inputSigla.pack(side="left")

        #botao consulta 
        self.frameButton = tkinter.Frame(self) 
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="Cunsulta equipe")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.pesquisaEquipe)

    def mostraJanela(self, titulo, msg):
            messagebox.showinfo(titulo, msg)

class ViewDadosCampeonato(tkinter.Toplevel):
    def __init__(self, controle, media, estudantes, equipes):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("Consulta campeonato")
        self.controle = controle

        #sigla do curso 
        self.frameSigla = tkinter.Frame(self)
        self.frameSigla.pack()
        self.labelSigla = tkinter.Label(self.frameSigla, text=f"Número de equipes: {equipes} \nNúmero total de estudantes: {estudantes}\nMédia de estudante por equipe: {media}")
        self.labelSigla.pack(side="left")


class CtrlEquipe():
    def __init__(self, contolePrincipal):
        if not os.path.isfile("Equipe.pickle"):
            self.listaEquipes =  []
        else:
            with open("Equipe.pickle", "rb") as f:
                self.listaEquipes = pickle.load(f)

        self.ctrlPrincipal = contolePrincipal
        self.time= []

#Cadastros
    def cadastraEquipe(self):
        listaNomeCurso = []
        listaCurso = self.ctrlPrincipal.ctrlCurso.getListaCurso()
        for curso in listaCurso:
            listaNomeCurso.append(curso.nome)
        self.viewCadastraEquipe = ViewCadastraEquipe(self, listaNomeCurso)

    def cadastraAluno(self, event):
        listaAluno = self.ctrlPrincipal.ctrlEstudante.getListaEstudante()

        curso = self.viewCadastraEquipe.escolhaCombo.get()
        nroMatAluno = self.viewCadastraEquipe.inputNroMatricula.get()
        
        for aluno in listaAluno:
            if int(aluno.nroMatricula) == int(nroMatAluno) and aluno.curso.nome == curso:
                msg = f"O aluno {aluno.nome} - {aluno.nroMatricula} cadastrado na equipe {aluno.curso.nome}"
                self.time.append(aluno)
                break
        else:
            msg = "Erro", "Numero de matricula nao pertence a esse curso!"

        self.viewCadastraEquipe.mostraJanela("Verifica aluno", msg)

    def criaEquipe(self, event):
        curso = self.viewCadastraEquipe.escolhaCombo.get()
        time = Equipe(self.time, curso)
        self.listaEquipes.append(time)

        self.time = []
        self.viewCadastraEquipe.destroy()
        self.viewCadastraEquipe.mostraJanela("Cadastro equipe", "Equipe cadstrada com sucesso")

#Consulta
    def consultaEquipe(self):
        self.viewConsultaEquipe = ViewConsultaEquipe(self)

    def pesquisaEquipe(self, event):
        cursoSigla = self.viewConsultaEquipe.inputSigla.get()
        listaCurso = self.ctrlPrincipal.ctrlCurso.getListaCurso()
        msg = ""
        cursoBuscado = None
        #pesquiso o nome do curso pela sigla
        for curso in listaCurso:
            if cursoSigla == curso.sigla:
                cursoBuscado = curso.nome 
                break
                
        if cursoBuscado is not None:
            for equipe in self.listaEquipes:
                if equipe.nome == cursoBuscado:
                    msg = f'Nome da equipe: {equipe.nome}\nJogadores: \n'
                    for jogador in equipe.jogadores:
                        msg+= f' {jogador.nome}\n'
                    break
            else:
                msg = f"Não existe equipe desse curso"
        else:
            msg = f"Sigla {cursoSigla} inesistente"

        self.viewConsultaEquipe.mostraJanela("Equipe consultada", msg)

    def salvaEquipe(self):
        if len(self.listaEquipes) != 0:
            with open("Equipe.pickle","wb") as f:
                pickle.dump(self.listaEquipes, f)

    def dadosCampeonato(self):
        nEquipe = len(self.listaEquipes)
        nEstudante = 0
        for equipe in self.listaEquipes:
            nEstudante += len(equipe.jogadores)

        media = nEstudante / nEquipe

        self.viewDadosCampeonato = ViewDadosCampeonato(self, media, nEstudante, nEquipe)

        



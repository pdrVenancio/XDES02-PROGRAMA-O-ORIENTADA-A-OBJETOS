import tkinter
from tkinter import ttk

class Equipe():
    def __init__(self, jogadores, nome) -> None:
        pass

class ViewCadastraEquipe(tkinter.Toplevel):
    def __init__(self, controle, listaCursos):
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
        self.combobox['values'] = listaCursos

        # Digitar o numedo de matricula dos alunos



class CtrlEquipe():
    def __init__(self, contolePrincipal):
        self.ctrlPrincipal = contolePrincipal
        self.listaEquipes = []

    def cadastraEquipe(self):
        listaCursos = self.ctrlPrincipal.ctrCurso.getListaCurso()
        self.viewCadastraEquipe = ViewCadastraEquipe(self, listaCursos)
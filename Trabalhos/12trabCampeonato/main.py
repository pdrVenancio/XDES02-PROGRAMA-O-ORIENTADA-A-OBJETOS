# Pedro Venâncio dos Santos
# Matrícula: 2023010066

import tkinter
import estudante
import curso
import equipe


class LimitePrincipal():

    def __init__(self, root, controle):
        self.root = root
        self.controle = controle

        self.menubar = tkinter.Menu(self.root)
        self.menuEquipe = tkinter.Menu(self.menubar, tearoff=0)
        self.menuSair = tkinter.Menu(self.menubar, tearoff=0)

        self.menuEquipe.add_command(label='Cadastrar Equipe', command=self.controle.cadastraEquipe)
        self.menuEquipe.add_command(label='Consultar Equipe', command=self.controle.consultaEquipe)
        self.menuEquipe.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label='Equipe', menu=self.menuEquipe)

        self.root.config(menu=self.menubar)

        self.frameNota = tkinter.Frame()
        self.frameNota.pack()

class ControlePrincipal():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.title("Campeonato de futebol")

        self.ctrlEquipe = equipe.CtrlEquipe(self)
        self.ctrlCurso = curso.CtrlCurso(self)
        self.ctrlEstudante = estudante.CtrlEstudante(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.mainloop()


    def cadastraEquipe(self):
        self.ctrlEquipe.cadastraEquipe()
        
    def consultaEquipe(self):
        self.ctrlEquipe.consultaEquipe()

    def salvaDados(self):
        self.ctrlEquipe.salvaEquipe()
        self.root.destroy()


if __name__ == "__main__":
    c = ControlePrincipal()

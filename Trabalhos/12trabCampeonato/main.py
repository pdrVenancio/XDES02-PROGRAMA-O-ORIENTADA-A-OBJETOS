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

        self.menuEquipe.add_command(label='Cadastrar Equipe', command=self.controle.cadastrarEquipe)
        self.menuEquipe.add_command(label='Consultar Equipe', command=self.controle.consultarEquipe)
        self.menubar.add_cascade(label='Equipe', menu=self.menuEquipe)

        self.root.config(menu=self.menubar)

        self.frameNota = tkinter.Frame()
        self.frameNota.pack()



class ControlePrincipal():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.title("Vendas do açougue")

        self.ctrlProduto = equipe.CtrlProduto(self)
        self.ctrlCliente = curso.CtrlCliente()
        self.ctrlNota = estudante.CtrlNotaFiscal(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.mainloop()


    def cadastrarEquipe(self):
        self.ctrlEquipe.cadastrarEquipe()
        
    def consultarEquipe(self):
        self.ctrlEquipe.consultarEquipe()

if __name__ == "__main__":
    c = ControlePrincipal()

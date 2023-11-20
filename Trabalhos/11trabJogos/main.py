from tkinter import *
from tkinter import simpledialog

import jogos

class Vew():
    def __init__(self, root, controle) -> None:
        self.controle = controle
        self.root = root

        self.root.geometry('700x700')

        self.menubar = Menu(self.root)

        self.jogoMenu = Menu(self.menubar)
        self.jogoMenu.add_command(label="Adicionar", command=self.controle.inserirJogo)
        self.jogoMenu.add_command(label="Consulta", command=self.controle.consultarJogo)
        self.jogoMenu.add_command(label="Avaliar", command=self.controle.avaliaJogo)
        self.jogoMenu.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Jogos", menu=self.jogoMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = Tk()

        self.ctrlJogo = jogos.CtrlJogo(self)

        self.vew = Vew(self.root, self)

        self.root.title("Musicas")

        self.root.mainloop()

    def inserirJogo(self):
        self.ctrlJogo.inserirJogo()

    def consultarJogo(self):
        self.ctrlJogo.consultarJogo()

    def avaliaJogo(self):
        self.ctrlJogo.avaliaJogo()

    def salvaDados(self):
        self.ctrlJogo.salvaJogo()
        self.root.destroy()


    
if __name__ == '__main__':
    c = ControlePrincipal()
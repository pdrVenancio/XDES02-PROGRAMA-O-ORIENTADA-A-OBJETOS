import tkinter
import peixe


class LimitePrincipal():
    def __init__(self, root, controle):
        self.root = root
        self.controle = controle

        self.menubar = tkinter.Menu(self.root)
        self.menu = tkinter.Menu(self.menubar, tearoff=0)
        self.menuSair = tkinter.Menu(self.menubar, tearoff=0)

        #sub menu
        self.menu.add_command(label='cadastra peixe', command=self.controle.cadastroPeixe)
        self.menu.add_command(label='mostra', command=self.controle.mostraPeixe)
        self.menu.add_command(label='cria comanda', command=self.controle.compraPeixe)
        self.menu.add_command(label='faturamento', command=self.controle.faturamento)

        self.menubar.add_cascade(label='menu', menu=self.menu)
        
        self.root.config(menu=self.menubar)

        self.frameNome = tkinter.Frame(self.root)
        self.frameNome.pack()
        self.labelNome = tkinter.Label(self.frameNome, text="Pedro Venâncio dos Santos - 2023010066")
        self.labelNome.pack(side="left")



class ControlePrincipal():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.title("Campeonato de futebol")

        self.ctrlPeixe = peixe.CtrlPeixe(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.mainloop()


    def cadastroPeixe(self):
        self.ctrlPeixe.cadastroPeixe()
        
    def mostraPeixe(self):
        self.ctrlPeixe.mostraPeixe()
        
    def compraPeixe(self):
        self.ctrlPeixe.compraPeixe()

    def faturamento(self):
        self.ctrlPeixe.faturamento()




if __name__ == "__main__":
    c = ControlePrincipal()
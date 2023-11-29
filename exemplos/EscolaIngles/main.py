import tkinter
import aluno

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x200')

        self.menubar = tkinter.Menu(self.root)
        self.menu = tkinter.Menu(self.menubar, tearoff=0)
        self.menuSair = tkinter.Menu(self.menubar, tearoff=0)
        
        # Menu Aluno
        self.menuAluno = tkinter.Menu(self.menubar)
        self.menuAluno.add_command(label="Cadastrar", command=self.controle.cadastraAluno)
        self.menuAluno.add_command(label="consulta", command=self.controle.consultaAluno)
        self.menubar.add_cascade(label="Aluno", menu=self.menuAluno) 

        self.root.config(menu=self.menubar) 

class ControlePrincipal():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.title("Escola ingles")

        self.ctrlAluno = aluno.CtrlAluno(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.mainloop()

    def cadastraAluno(self):
        self.ctrlAluno.cadastroAluno()

    def consultaAluno(self):
        self.ctrlAluno.consultaAluno()

if __name__ == "__main__":
    c = ControlePrincipal()

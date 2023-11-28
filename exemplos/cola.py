#Main 
import tkinter
import arq1
import arq2
import arq3

class LimitePrincipal():
    def __init__(self, root, controle):
        self.root = root
        self.controle = controle

        self.menubar = tkinter.Menu(self.root)
        self.menu1 = tkinter.Menu(self.menubar, tearoff=0)
        self.menuSair = tkinter.Menu(self.menubar, tearoff=0)

        #sub menu
        self.menu1.add_command(label='1', command=self.controle.funcao1)
        self.menu1.add_command(label='2', command=self.controle.funcao2)
        self.menu1.add_command(label="3", command=self.controle.funcao3)
        self.menu1.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label='menu', menu=self.menu1)
        
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

        self.ctrlEquipe = arq3.CtrlEquipe(self)
        self.ctrlCurso = arq2.CtrlCurso(self)
        self.ctrlEstudante = arq1.CtrlEstudante(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.mainloop()


    def funcao1(self):
        self.ctrlEquipe.funcao1()
        
    def funcao2(self):
        self.ctrlEquipe.funcao2()
    
    def funcao3(self):
        self.ctrlEquipe.funcao3()

    def salvaDados(self):
        self.ctrlEquipe.salvaEquipe()
        self.root.destroy()


if __name__ == "__main__":
    c = ControlePrincipal()

#Classe

class Classe():
    def __init__(self, a1, a2, a3) -> None:
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3

    @property
    def a1(self):
        return self.__a1
    
    @property
    def a2(self):
        return self.__a2
    
    @property
    def a3(self):
        return self.__a3

#View
from tkinter import messagebox, ttk

class View(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("")
        self.controle = controle 
#submenus
#combobox
        self.frameAlgum1 = tkinter.Frame(self)
        self.frameAlgum1.pack()
        self.labelAlgum1frameAlgum1 = tkinter.Label(self.frameAlgum1, text="Escolha: ")
        self.labelAlgum1frameAlgum1.pack(side="left")
        self.escolhaCombo = tkinter.StringVar()
        self.combobox = ttk.Combobox(self.frameAlgum1, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCombo

#Entry
        self.frameAlgum2 = tkinter.Frame(self)
        self.frameAlgum2.pack()
        self.labelAlgum2 = tkinter.Label(self.frameAlgum2, text="Algum2: ")
        self.labelAlgum2.pack(side="left")
        self.inputAlgum2 = tkinter.Entry(self.frameAlgum2, width=20)
        self.inputAlgum2.pack(side="left")

#botao
        self.frameButton = tkinter.Frame(self) 
        self.frameButton.pack()
        self.buttonSubmit = tkinter.Button(self.frameButton, text="")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.funcaoChamada)

#listBox
        self.frameMusica = tkinter.Frame(self)
        self.framePlaylist.pack()
        self.labelMus = tkinter.Label(self.frameMusica, text="Escolha o Musica: ")
        self.labelMus.pack(side="left")
        self.listbox = tkinter.Listbox(self.frameMusica)
        self.listbox.pack(side="left")
        self.combobox.bind("<<ComboboxSelected>>", self.controle.musicaPorArtista)

#mostra janela   
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

#padaro ctrl
class CtrlAlgum():
    def __init__(self, controlePrincipal):
        self.listaAlgums = []
        self.ctrlPrincipal = controlePrincipal

#salva ctrl
import pickle, os.path
class Ctrl1():
    def __init__(self ,controlePrincipal):
        if not os.path.isfile("1.pickle"):
            self.lista1 =  []
        else:
            with open("1.pickle", "rb") as f:
                self.lista1 = pickle.load(f)
        
        self.ctrlPrincipal = controlePrincipal

#funcao para salvar 
    def salva1(self):
            if len(self.lista1s) != 0:
                with open("1s.pickle","wb") as f:
                    pickle.dump(self.lista1s, f)
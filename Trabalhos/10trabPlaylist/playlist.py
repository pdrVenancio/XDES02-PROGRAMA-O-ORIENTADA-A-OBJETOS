from musica import Musica
from tkinter import *
from tkinter import messagebox

class Playlist:
    def __init__(self, nome):
        self.__nome = nome

        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def musicas(self):
        return self.__musicas
    
    def addMusica(self, musica):
        self.__musicas.append(musica)


class LimiteInserePlaylist(Toplevel):
    def __init__(self, controle, listaMusicas):
        Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Playlist")
        self.controle = controle

        # Aqui criamos algumas partes da janelinha, como rótulos (labels), caixas de texto, combobox e botões.
        self.frameNomePlaylist = Frame(self)
        self.framePlaylist = Frame(self)
        self.frameButton = Frame(self)
        self.frameNomePlaylist.pack()
        self.framePlaylist.pack()
        self.frameButton.pack()

        # Pega nome da playlist
        self.labelNomePlaylist = Label(self.frameNomePlaylist, text="Informe o nome da playlist: ")
        self.labelNomePlaylist.pack(side="left")
        self.inputNomePlaylist = Entry(self.frameNomePlaylist, width=20)
        self.inputNomePlaylist.pack(side="left")

        # Add musicas
        self.labelPlaylist = Label(self.framePlaylist, text="Escolha a Musicas: ")
        self.labelPlaylist.pack(side="left")
        self.escolhaCombo = StringVar()
        self.combobox = Combobox(self.framePlaylist, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaMusicas

        # Rótulos, listbox e botões
    
        self.buttonInsere = Button(self.frameButton, text="Insere Musica")
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = Button(self.frameButton, text="Cria Playlist")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)

    # Uma função para mostrar mensagens na tela.
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class VewMostraPlaylists():
    def __init__(self) -> None:
        messagebox.showinfo("Lista de turmas", str)

class CtrlPlaylist():
    pass
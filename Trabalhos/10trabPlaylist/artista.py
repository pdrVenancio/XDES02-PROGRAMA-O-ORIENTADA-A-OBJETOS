from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

from album import *
from playlist import *
from musica import *

class Artista:
    def __init__(self, nome):
        self.__nome = nome
        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def albuns(self):
        return self.__albuns
    
    @property
    def musicas(self):
        return self.__musicas

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)

    
class VewInsereArtista(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = Frame(self)
        self.frameButton = Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")

        self.inputNome = Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class VewMostraArtista():
    def __init__(self, str):
        messagebox.showinfo('Lista de artistas', str)

class CtrlArtista():
    def __init__(self) -> None:
        self.listaArtistas = []

    def consultarArtistas(self):
        answer = simpledialog.askstring("Consultar albuns", "Qual o Artista??",
                                            parent=self.root.janela)
    
        for artista in self.listaArtistas:
            if answer == str(artista.nome):
                msg = f"artistas de nome {answer}:\n"
                msg += artista.albuns + "\n"
                self.view.mostraJanela("artistas ENCONTRADO!!!!!!!!", msg)
        else:
            self.view.mostraJanela("",f"artistas nao cadastrado! {answer}")
        
    
    def inserirArtistas(self):
        self.limiteIns = VewInsereArtista(self)
    
    def mostraArtistas(self):
        str = "Nome\n"
        for art in self.listaArtistas:
            str += art.nome + "\n"
        self.vewLista = VewMostraArtista(str)
    
    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso!')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

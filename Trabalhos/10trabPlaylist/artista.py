from tkinter import *
from tkinter import messagebox

from album import Album
from musica import Musica

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

class VewConsultaArtista(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameBusca = Frame(self)
        self.frameButton = Frame(self)
        self.frameBusca.pack()
        self.frameButton.pack()

        self.labelBusca = Label(self.frameBusca, text="Buscar Artista: ")
        self.labelBusca.pack(side="left")

        self.inputBusca = Entry(self.frameBusca, width=20)
        self.inputBusca.pack(side="left")

        self.buttonSubmit = Button(self.frameButton, text="Buscar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.buscaHandler)

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
    def __init__(self, controlePrincipal):
        self.listaArtistas = [Artista("p"), Artista("o")]
        self.ctrlPrincipal = controlePrincipal
    
    def getListaMusicasPorArtista(self, artista):
        self.listaMusicas = []

        if artista is None:
            return self.listaMusicas
        else:
            for art in self.listaArtistas:
                if art.nome == artista:
                    # Adiciona as músicas do artista à lista
                    self.listaMusicas.extend(art.musicas)

            return self.listaMusicas

    def getListaNomeArtista(self):
        self.listaNomeArtista = []
        for art in self.listaArtistas:
            self.listaNomeArtista.append(art.nome)
        
        return self.listaNomeArtista

    def getMusica(self, musicaBuscada):
        for art in self.listaArtistas:
            if art.musica == musicaBuscada:
                return musicaBuscada
            
    def getListaArtista(self):# para q a lista de artista possa ser acessada por outros arquivos
        return self.listaArtistas

    def consultarArtistas(self):
        self.listaAlbuns = self.ctrlPrincipal.ctrlAlbum.getListaAlbum()
        self.vewConsulta = VewConsultaArtista(self)      
    
    def inserirArtistas(self):
        self.limiteIns = VewInsereArtista(self)
    
    def mostraArtistas(self):
        str = "Nome\n"
        for art in self.listaArtistas:
            str += art.nome + "\n"
        self.vewLista = VewMostraArtista(str)
    
    def buscaHandler(self, event):
        artista = self.vewConsulta.inputBusca.get()

        for art in self.listaArtistas:
            if art.nome == artista:
                str = f'O artista {artista} possue os seguintes albuns:\n'
                for alb in self.listaAlbuns:
                    if alb.artista == artista:
                        str += f"\n{alb.titulo}"
            else:
                str =  f'Artista {artista} nao existe na lista!'
            
            messagebox.showinfo('Cunsulta', str)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        cont = 1
        for art in self.listaArtistas:
            if art.nome == nome:
                str = 'Artista ja cadastrado' 
                cont = 0
        if cont == 1:  
            artista = Artista(nome)
            self.listaArtistas.append(artista)
            str = f"Artista {nome} cadastrado com sucesso"
        
        
        self.limiteIns.mostraJanela('Cadastro artista', str)
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

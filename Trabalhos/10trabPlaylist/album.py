from musica import Musica

from tkinter import *
from tkinter import messagebox

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def faixas(self):
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        musica = Musica(titulo, artista, self)
        self.__faixas.append(musica)

class VewInsereAlbum(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Insere album")
        self.controle = controle

        self.frameTitulo = Frame(self)
        self.frameArtista = Frame(self)
        self.frameAno = Frame(self)
        self.frameMusica= Frame(self)
        self.frameButton = Frame(self)
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameMusica.pack()
        self.frameButton.pack()
        

        self.labelTitulo = Label(self.frameTitulo, text="Titulo: ")
        self.labelTitulo.pack(side="left")
        
        self.labelArtista = Label(self.frameArtista, text="Artista: ")
        self.labelArtista.pack(side="left")
        self.labelAno = Label(self.frameAno, text="Ano: ")
        self.labelAno.pack(side="left")
        self.labelMusica = Label(self.frameMusica, text="Musica: ")
        self.labelMusica.pack(side="left")

        self.inputTitulo = Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        self.inputArtista = Entry(self.frameArtista, width=20)
        self.inputArtista.pack(side="left")
        self.inputAno = Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")
        self.inputMusica = Entry(self.frameMusica, width=20)
        self.inputMusica.pack(side="left")


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

class VewConsultaAlbum(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta album")
        self.controle = controle

        self.frameBusca = Frame(self)
        self.frameButton = Frame(self)
        self.frameBusca.pack()
        self.frameButton.pack()

        self.labelBusca = Label(self.frameBusca, text="Buscar Album: ")
        self.labelBusca.pack(side="left")

        self.inputBusca = Entry(self.frameBusca, width=20)
        self.inputBusca.pack(side="left")

        self.buttonSubmit = Button(self.frameButton, text="Buscar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.buscaHandler)


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
    
class VewMostraAlbum():
    def __init__(self, str):
        messagebox.showinfo('Lista de álbuns', str)

class CtrlAlbum():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlbuns = []

    #deixa  a lista de album para acessar outras
    def getListaAlbum(self):
        return self.listaAlbuns

    def consultaAlbum(self):
       self.vewConsultar = VewConsultaAlbum(self)

    def inserirAlbuns(self):
        self.nomeArts = self.ctrlPrincipal.ctrlArtista.getListaArtista()
        self.limiteIns = VewInsereAlbum(self)
    
    def buscaHandler(self,event):
        str = "Lsita de musicas:\n"
        titulo = self.vewConsultar.inputBusca.get()
        for alb in self.listaAlbuns:
            if alb.titulo == titulo:
                for faixa in alb.faixas:
                    str += f"\n  {faixa.titulo}"
    
        self.vewLista = VewMostraAlbum(str)
    
    def enterHandler(self, event):
        #verifica se o artista foi registrado
        artista = self.limiteIns.inputArtista.get()
        for art in self.nomeArts:
            if artista == art.nome :
                cont = 0
                break
            else: 
                cont = 1

        if cont == 0:
            cont = 1
            titulo = self.limiteIns.inputTitulo.get()
            for album in self.listaAlbuns:
                if titulo == album.titulo:
                    cont = 0
                    break

            # caso seja a criação de um novo album
            if cont == 1:
                titulo = self.limiteIns.inputTitulo.get()
                artista = self.limiteIns.inputArtista.get()
                ano = self.limiteIns.inputAno.get()
                album = Album(titulo, artista, ano)
                self.listaAlbuns.append(album)
                musica = self.limiteIns.inputMusica.get()
                self.ctrlPrincipal.ctrlMusica.addMusica(musica, artista, titulo)
                if musica:
                    album.addFaixa(musica, artista)

            # caso for a inserção de uma musica em um album ja existente
            elif cont == 0:
                
                musica = self.limiteIns.inputMusica.get()
                
                self.ctrlPrincipal.ctrlMusica.addMusica(musica, artista, titulo)
                artista = self.limiteIns.inputArtista.get()
                if musica:
                    album.addFaixa(musica, artista)

            str = "Album registrado com sucesso"
        else:
            str = "Artista não registrado!"
        self.limiteIns.mostraJanela('Inserção', str)
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputArtista.delete(0, len(self.limiteIns.inputArtista.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        self.limiteIns.inputMusica.delete(0, len(self.limiteIns.inputMusica.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
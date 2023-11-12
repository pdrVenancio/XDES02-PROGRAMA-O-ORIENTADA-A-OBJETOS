from artista import *
from playlist import *
from musica import *
from tkinter import *
from tkinter import messagebox

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []
        artista.addAlbum(self)

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
        nroFaixa = len(self.__faixas)
        musica = Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(musica)

class VewInsereAlbum(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Album")
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
    ...
    
class VewMostraAlbum():
    def __init__(self, str):
        messagebox.showinfo('Lista de álbuns', str)

class CtrlAlbum():
    def __init__(self) -> None:
        self.listaAlbuns = []
    
    def consultaAlbum(self):
       ...

    def inserirAlbuns(self):
        self.limiteIns = VewInsereAlbum(self)
    
    def mostrarAlbum(self):
        str = "Lsita de albuns:\n"
        for alb in self.listaAlbuns:
            str += f"Titulo: {alb.titulo} \nArtista: {alb.artista}\nAno: {alb.ano}\nFaixas:"
            for faixa in alb.faixas:
                str += f"\n  {faixa.titulo}"
            str += "\n\n"

        self.vewLista = VewMostraAlbum(str)
    
    def enterHandler(self, event):
        cont = 1
        titulo = self.limiteIns.inputTitulo.get()
        for album in self.listaAlbuns:
            if titulo == album.titulo:
                cont = 0
        
        if cont == 1:
            titulo = self.limiteIns.inputTitulo.get()
            artista = self.limiteIns.inputArtista.get()
            ano = self.limiteIns.inputAno.get()
            album = Album(titulo, artista, ano)
            self.listaAlbuns.append(album)

            musica = self.limiteIns.inputMusica.get()
            if musica:
                album.addFaixa(musica, artista)
        
        elif cont == 0:
            musica = self.limiteIns.inputMusica.get()
            artista = self.limiteIns.inputArtista.get()
            if musica:
                album.addFaixa(musica, artista)


        self.limiteIns.mostraJanela('Sucesso', 'Álbum cadastrado com sucesso!')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputArtista.delete(0, len(self.limiteIns.inputArtista.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()
import musica
from tkinter import *
from tkinter import messagebox

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
    
class VewInsereArtista(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        # Aqui criamos algumas partes da janelinha, como rótulos (labels), caixas de texto e botões.
        self.frameNome = Frame(self)
        self.frameButton = Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        # Rótulos
        self.labelNome = Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")

        # Caixas de texto
        self.inputNome = Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        # Botões
        self.buttonSubmit = Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    # Uma função para mostrar mensagens na tela.
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class VewMostraArtista():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

class CtrArtista():
    def __init__(self) -> None:
        self.listaArtistas = []
    
    def getArtista(self):
        ...
    
    def mostraArtistas(self):
        str = "Nome\n"
        for art in self.listaArtistas:
            str += art.nome + "\n"
        self.vewLista = VewInsereArtista(str)
    
    # Pega os dados do formulario
    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtistas.append(artista)
        self.limiteIns.mostrarjamela('Sucesso', 'Artista cadastrado com sucesso!')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()
    


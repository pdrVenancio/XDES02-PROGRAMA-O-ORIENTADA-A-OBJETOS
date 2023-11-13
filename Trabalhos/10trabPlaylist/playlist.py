from musica import Musica
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



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


class VewInserePlaylist(Toplevel):
    def __init__(self, controle, listaMusicas, listaNomeArtistas):
        Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Playlist")
        self.controle = controle

        # Aqui criamos algumas partes da janelinha, como rótulos (labels), caixas de texto, combobox e botões.
        self.frameNomePlaylist = Frame(self)
        self.framePlaylist = Frame(self)
        self.frameMusica = Frame(self)
        self.frameButton = Frame(self)
        self.frameNomePlaylist.pack()
        self.framePlaylist.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        # Pega nome da playlist
        self.labelNomePlaylist = Label(self.frameNomePlaylist, text="Informe o nome da playlist: ")
        self.labelNomePlaylist.pack(side="left")
        self.inputNomePlaylist = Entry(self.frameNomePlaylist, width=20)
        self.inputNomePlaylist.pack(side="left")

        # Seleciona o artista 
        self.labelPlaylist = Label(self.framePlaylist, text="Escolha o artista: ")
        self.labelPlaylist.pack(side="left")
        self.escolhaCombo = StringVar()
        self.combobox = ttk.Combobox(self.framePlaylist, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomeArtistas

    

        #lista de musicas baseado nos artistas
        self.labelMus = Label(self.frameMusica, text="Escolha o Musica: ")
        self.labelMus.pack(side="left")
        self.listbox = Listbox(self.frameMusica)
        self.listbox.pack(side="left")
        """ for musica in listaMusicas:
            self.listbox.insert(END, musica.titulo) """
        
        self.combobox.bind("<<ComboboxSelected>>", self.controle.musicaPorArtista)
            

        # Rótulos, listbox e botões
        self.buttonCria = Button(self.frameButton, text="Cria Playlist")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)

    # Uma função para mostrar mensagens na tela.
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class VewMostraPlaylists():
    def __init__(self, str):
        messagebox.showinfo("Lista de turmas", str)

class CtrlPlaylist():
    def __init__(self, controlePrincipal) :
        self.listaPlaylist = []
        self.ctrlPrincipal = controlePrincipal

    def inserirPlaylist(self):
        #artista = self.vewInserir.escolhaCombo.get()
        listaMusicas = self.ctrlPrincipal.ctrlMusica.getListaMusicas()
        listaNomeArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomeArtista()
        self.vewInserir = VewInserePlaylist(self, listaMusicas, listaNomeArtistas)
    
    def musicaPorArtista(self, event):
        self.vewInserir.listbox.delete(0, END) # clear listbox
        
        artistaSelecionado = self.vewInserir.escolhaCombo.get()

        listaMusicas = self.ctrlPrincipal.ctrlMusica.getListaMusicas()
        for musica in listaMusicas:
            if musica.artista == artistaSelecionado:
                self.vewInserir.listbox.insert(END, musica.titulo)
                
       
    def criaPlaylist(self, event):
        nome = self.vewInserir.inputNomePlaylist.get()
        #artistaSelecionado = self.vewInserir.escolhaCombo.get()
        #artista = self.ctrlPrincipal.ctlrArtista.getArtista(artistaSelecionado)

        playlist = Playlist(nome)
        self.listaPlaylist.append(playlist)
        self.vewInserir.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.vewInserir.destroy()
    
    def inserirMusica(self, event):
        musicaSelecionada = self.vewInserir.listbox.get(ACTIVE)
        musica = self.ctrlPrincipal.ctrlArtista.getMusica(musicaSelecionada)
        self.listaPlaylist.append(musica)

        for musi in self.listaPlaylist:
            str = "lista da playlist\n"
            str += f"{musi.nome}\n"
            str += musi

        self.vewInserir.mostraJanela("criação de Playlist", str)


    
        
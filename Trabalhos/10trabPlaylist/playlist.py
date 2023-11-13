from musica import Musica
from tkinter import *
from tkinter import messagebox
from tkinter import ttk



class Playlist:
    def __init__(self, nome , musicas):
        self.__nome = nome
        self.__musicas = musicas

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def name(self, string):
        self.__nome = string
    
    @property
    def musicas(self):
        return self.__musicas



class VewInserePlaylist(Toplevel):
    def __init__(self, controle, listaNomeArtistas):
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

        self.combobox.bind("<<ComboboxSelected>>", self.controle.musicaPorArtista)
        
        # botões
        self.buttonIns = Button(self.frameButton, text="Inserir Musica")
        self.buttonIns.pack(side="left")
        self.buttonIns.bind("<Button>", controle.inserirMusica)
            
        self.buttonCria = Button(self.frameButton, text="Cria Playlist")
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)

    # Uma função para mostrar mensagens na tela.
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class VewMostraPlaylists():
    def __init__(self, str):
        messagebox.showinfo("Playlists", str)

class VewConsultaPlaylist(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameBusca = Frame(self)
        self.frameButton = Frame(self)
        self.frameBusca.pack()
        self.frameButton.pack()

        self.labelBusca = Label(self.frameBusca, text="Buscar Playlist: ")
        self.labelBusca.pack(side="left")

        self.inputBusca = Entry(self.frameBusca, width=20)
        self.inputBusca.pack(side="left")

        self.buttonSubmit = Button(self.frameButton, text="Buscar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.buscaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)           

class CtrlPlaylist():
    def __init__(self, controlePrincipal) :
        self.listaPlaylist = []
        self.ctrlPrincipal = controlePrincipal

    def inserirPlaylist(self):
        self.musicasAddPlaylist = []
        listaNomeArtistas = self.ctrlPrincipal.ctrlArtista.getListaNomeArtista()
        self.vewInserir = VewInserePlaylist(self, listaNomeArtistas)
    
    def musicaPorArtista(self, event):
        self.vewInserir.listbox.delete(0, END) # clear listbox

        artistaSelecionado = self.vewInserir.escolhaCombo.get()

        listaMusicas = self.ctrlPrincipal.ctrlMusica.getListaMusicas()
        for musica in listaMusicas:
            if musica.artista == artistaSelecionado:
                self.vewInserir.listbox.insert(END, musica.titulo)
                    
    def criaPlaylist(self, event):
        
        nome = self.vewInserir.inputNomePlaylist.get()
        
        playlist = Playlist(nome, self.musicasAddPlaylist)
        self.listaPlaylist.append(playlist)
        self.vewInserir.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.vewInserir.withdraw()
    
    def inserirMusica(self, event):  
        self.musicasAddPlaylist = []
        musicaSelecionada = self.vewInserir.listbox.get(ACTIVE)
        musica = self.ctrlPrincipal.ctrlMusica.getMusica(musicaSelecionada)
        self.musicasAddPlaylist.append(musica)

        str = "Musica inserida:\n"
        str += f"{musica.titulo}\n"

        self.vewInserir.mostraJanela("criação de Playlist", str)

    def mostraPlaylist(self):
        str = "Playlists: \n\n"
        for playlist in self.listaPlaylist:
            str += f"{playlist.nome}:\n"
            for musica in playlist.musicas:
                str += f"  {musica.titulo}\n"
                
        self.vewLista = VewMostraPlaylists(str)

    def consultaPlaylist(self):
        self.vewConsulta = VewConsultaPlaylist(self)    

    def buscaHandler(self, event):
        nomePlaylist = self.vewConsulta.inputBusca.get()

        for playlist in self.listaPlaylist:
          if playlist.nome == nomePlaylist:
            str = f"{playlist.nome}:\n"
            for musica in playlist.musicas:
                str += f"  {musica.titulo}\n"
            
        messagebox.showinfo('Cunsulta', str)  
    
        
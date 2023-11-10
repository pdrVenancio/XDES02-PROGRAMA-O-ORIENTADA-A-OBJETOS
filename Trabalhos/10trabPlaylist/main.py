from tkinter import *
import artista, album, playlist


class Vew():
    def __init__(self, root, controle) -> None:
        self.controle = controle
        self.root =root

        self.root.geometry('500x500')

        self.menubar = Menu(self.root)

        self.artistaMenu = Menu(self.menubar)
        self.artistaMenu.add_command(label="Adicionar", command=self.controle.inserirArtistas)
        self.artistaMenu.add_command(label="Mostra", command=self.controle.mostraArtistas)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        self.albumMenu = Menu(self.menubar)
        self.albumMenu.add_command(label="Adicionar", command=self.controle.inserirAlbums)
        self.albumMenu.add_command(label="Mostra", command=self.controle.mostraAlbums)
        self.menubar.add_cascade(label="Album", menu=self.albumMenu)

        self.playlistMenu = Menu(self.menubar)
        self.playlistMenu.add_command(label="Adicionar", command=self.controle.inserirPlaylists)
        self.playlistMenu.add_command(label="Mostra", command=self.controle.mostraPlaylists)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.root.confg(menu=self.menubar)

class Controle:
    def __init__(self) -> None:
        
        self.root = Tk()

        self.ctrAlbum = album.CtrlAlbum()
        self.ctrArtista = artista.CtrlArtista()
        self.ctrPlaylist = playlist.CtrlPlaylist()

        self.vew = Vew(self.root, self)

        self.root.title("Musicas")
        self.root.mainloop()
    
        


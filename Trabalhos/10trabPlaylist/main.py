from tkinter import *
from tkinter import simpledialog

import artista, playlist, album, musica

class Vew():
    def __init__(self, root, controle) -> None:
        self.controle = controle
        self.root = root

        self.root.geometry('700x700')

        self.menubar = Menu(self.root)

        self.artistaMenu = Menu(self.menubar)
        self.artistaMenu.add_command(label="Adicionar", command=self.controle.inserirArtistas)
        self.artistaMenu.add_command(label="Consulta", command=self.controle.consultarArtistas)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        self.albumMenu = Menu(self.menubar)
        self.albumMenu.add_command(label="Adicionar", command=self.controle.inserirAlbum)
        self.albumMenu.add_command(label="Mostar", command=self.controle.mostrarAlbum)
        self.albumMenu.add_command(label="Consulta", command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Album", menu=self.albumMenu)
        

        self.playlistMenu = Menu(self.menubar)
        self.playlistMenu.add_command(label="Adicionar", command=self.controle.inserirPlaylist)
        self.playlistMenu.add_command(label="Mostra", command=self.controle.mostraPlaylist)
        self.playlistMenu.add_command(label="Consulta", command=self.controle.consultaPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = Tk()

        self.ctrlAlbum = album.CtrlAlbum(self)
        self.ctrlArtista = artista.CtrlArtista(self)
        self.ctrlMusica = musica.CtrlMusica(self)

        self.ctrlPlaylist = playlist.CtrlPlaylist(self)

        self.vew = Vew(self.root, self)

        self.root.title("Musicas")

        self.root.mainloop()

    def inserirArtistas(self):
        self.ctrlArtista.inserirArtistas()

    def consultarArtistas(self):
        self.ctrlArtista.consultarArtistas()

    def inserirAlbum(self):
        self.ctrlAlbum.inserirAlbuns()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()

    def mostrarAlbum(self):
        self.ctrlAlbum.mostrarAlbum()

    def inserirPlaylist(self):
        self.ctrlPlaylist.inserirPlaylist()

    def mostraPlaylist(self):
        self.ctrlPlaylist.mostraPlaylist()
    
    def consultaPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()

if __name__ == '__main__':
    c = ControlePrincipal()

from tkinter import *
from tkinter import simpledialog

import artista, playlist, album

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
        self.albumMenu.add_command(label="Adicionar", command=self.controle.inserirAlbuns)
        self.albumMenu.add_command(label="Mostar", command=self.controle.mostrarAlbum)
        self.albumMenu.add_command(label="Consulta", command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Album", menu=self.albumMenu)
        

        self.playlistMenu = Menu(self.menubar)
        self.playlistMenu.add_command(label="Adicionar", command=self.controle.inserirPlaylists)
        self.playlistMenu.add_command(label="Mostra", command=self.controle.mostraPlaylists)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = Tk()

        self.ctrlAlbum = album.CtrlAlbum(self)
        self.ctrlArtista = artista.CtrlArtista(self)
        self.ctrlPlaylist = playlist.CtrlPlaylist()

        self.vew = Vew(self.root, self)

        self.root.title("Musicas")

        self.root.mainloop()

    def inserirArtistas(self):
        self.ctrlArtista.inserirArtistas()

    def consultarArtistas(self):
        self.ctrlArtista.consultarArtistas()

    def inserirAlbuns(self):
        self.ctrlAlbum.inserirAlbuns()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()

    def mostrarAlbum(self):
        self.ctrlAlbum.mostrarAlbum()

    def inserirPlaylists(self):
        self.ctrlPlaylist.inserirPlaylists()

    def mostraPlaylists(self):
        self.ctrlPlaylist.mostraPlaylists()

if __name__ == '__main__':
    c = ControlePrincipal()

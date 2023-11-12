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
    
class Musica:
    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

        artista.addMusica(self)

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def album(self):
        return self.__album
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa
    
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

if __name__ == "__main__":
    listaAlbuns = []
    art1 = Artista('coldplay')
    album1 = Album('album1', art1, 2011)
    album1.addFaixa('m1')
    album1.addFaixa('m2')

    listaAlbuns.append(album1)

    album2 = Album('album2', art1, 2011)
    album2.addFaixa('m1')
    album2.addFaixa('m2')

    listaAlbuns.append(album2)


    for m in art1.musicas:
        print(m.titulo)

    # 1) criar eexibir uma playlist com as musicas do album 1
    pl1 = Playlist('pl1')
    for musica in album1.faixas:
        pl1.addMusica(musica)
    print(f'Playlist {pl1.nome}')
    for musica in pl1.musicas:
        print(musica.titulo)
    print()
    # 2) criar e exibir uma playlist com todas as musicas
    pl2 = Playlist('pl2')
    for album in listaAlbuns:
        for musica in album.faixas:
            pl2.addMusica(musica)

    print(f'Playlist {pl2.nome}')
    for musica in pl2.musicas:
        print(musica.titulo)
    print()

# 3) criar e exibir uma playlist contendo uma musica de cada album
    pl3 = Playlist('pl3')
    for album in listaAlbuns:
        pl3.addMusica(album.faixas[0])  # Adding the first track of each album

    print(f'Playlist {pl3.nome}')
    for musica in pl3.musicas:
        print(musica.titulo)

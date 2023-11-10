import musica

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

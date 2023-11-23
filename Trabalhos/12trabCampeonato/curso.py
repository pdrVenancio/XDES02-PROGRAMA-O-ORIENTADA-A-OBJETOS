import tkinter

class Curso:
    def __init__(self, sigla, nome) -> None:
        self.__sigla = sigla
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__nome

class CtrlCurso():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        c1 = Curso("CCO", "Ciencia da Computacao")
        c2 = Curso("SIN", "Sistemas de Informacao")
        c3 = Curso("EEL", "Engenharia Eletrica")
        self.listaCurso = []
        self.listaCurso.append(c1)
        self.listaCurso.append(c2)
        self.listaCurso.append(c3)
    
    def getListaCurso(self):
        return self.listaCurso
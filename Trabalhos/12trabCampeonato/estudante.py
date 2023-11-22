import tkinter

class Estudante:
    def __init__(self, nroMatricula, nome, curso) -> None:
        self.__nroMatricula = nroMatricula
        self.__nome = nome
        self.__curso = curso

    @property
    def nroMatricula(self):
        return self.__nroMatricula
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def curso(self):
        return self.__curso
    

class CtrlEstudante():
    def __init__(self, controlePrincipal) -> None:
        self.ctrlPrincipal = controlePrincipal
        self.listaEstudante
        self.listaEstudante.append(Estudante(1001, "José da Silva", c1))
        self.listaEstudante.append(Estudante(1002, "João de Souza", c1))
        self.listaEstudante.append(Estudante(1003, "Rui Santos", c2))
        self.listaEstudante.append(Estudante(1004, "José", c1))
        self.listaEstudante.append(Estudante(1005, "João ", c1))
        self.listaEstudante.append(Estudante(1006, "Rui", c2))
        self.listaEstudante.append(Estudante(1007, "Silva", c1))
        self.listaEstudante.append(Estudante(1008, "JSouza", c1))
        self.listaEstudante.append(Estudante(1009, "Santos", c2))
        self.listaEstudante.append(Estudante(1009, "Pedro", c2))

    def getListaEstudantes(self):
        return self.getListaEstudantes


# Aqui em cima, estamos chamando alguns amigos que vão nos ajudar.
import tkinter as tk
from tkinter import messagebox
import estudante as est
import disciplina as disc
import turma as trm

# Agora, vamos desenhar uma janelinha bonita e adicionar botões nela.
class LimitePrincipal():
    def __init__(self, root, controle):
        # Aqui dizemos que essa janelinha vai depender de outras coisas.
        self.controle = controle
        self.root = root
        # Agora, a janelinha vai ter um tamanho especial.
        self.root.geometry('300x250')  

        # Vamos adicionar uma barra lá em cima, como num restaurante, com botões dentro.
        self.menubar = tk.Menu(self.root)        

        # Botões para Estudantes
        self.estudanteMenu = tk.Menu(self.menubar)
        self.estudanteMenu.add_command(label="Adicionar", \
                    command=self.controle.insereEstudantes)
        self.estudanteMenu.add_command(label="Mostrar", \
                    command=self.controle.mostraEstudantes)
        self.menubar.add_cascade(label="Estudante", \
                    menu=self.estudanteMenu)

        # Botões para Disciplinas
        self.discipMenu = tk.Menu(self.menubar)
        self.discipMenu.add_command(label="Adicionar", \
                    command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="Mostrar", \
                    command=self.controle.mostraDisciplinas)
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discipMenu)

        # Botões para Turmas
        self.turmaMenu = tk.Menu(self.menubar)
        self.turmaMenu.add_command(label="Adicionar", \
                    command=self.controle.insereTurmas)
        self.menubar.add_cascade(label="Turma", \
                    menu=self.turmaMenu)        

        # Dizemos que a barra lá em cima pertence à nossa janelinha.
        self.root.config(menu=self.menubar)

# Agora, vamos criar o chefinho que vai controlar tudo.
class ControlePrincipal():       
    def __init__(self):
        # Aqui dizemos ao computador para criar uma janelinha.
        self.root = tk.Tk()

        # Criamos uns "chefinhos" que vão cuidar dos estudantes, disciplinas e turmas.
        self.ctrlEstudante = est.CtrlEstudante()
        self.ctrlDisciplina = disc.CtrlDisciplina()
        self.ctrlTurma = trm.CtrlTurma(self)

        # Criamos uma janelinha bonita usando a classe LimitePrincipal.
        self.limite = LimitePrincipal(self.root, self) 

        # Damos um nome para a janelinha.
        self.root.title("Exemplo MVC")
        # E começamos a mostrar a janelinha para o usuário.
        self.root.mainloop()
       
    # Essas são como as ordens que o chefinho dá aos "chefinhos" dos estudantes, disciplinas e turmas.
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes()

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def insereTurmas(self):
        self.ctrlTurma.insereTurmas()

if __name__ == '__main__':
    c = ControlePrincipal()

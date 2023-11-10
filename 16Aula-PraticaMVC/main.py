# Olá amiguinho! Este é um código em Python que usa o Tkinter para fazer um programinha com botõezinhos e janelas.

# Aqui em cima, estamos falando para o computador que queremos usar uma biblioteca chamada Tkinter.
import tkinter as tk
from tkinter import messagebox
import estudante as est
import disciplina as dis

# Essas duas linhas estão dizendo para o programa que temos outras coisinhas (módulos) chamadas estudante e disciplina,
# mas não mostramos o que tem nelas aqui.

# Agora, vamos fazer um tipo de desenho na tela. Imagina que estamos criando uma janelinha bonita.
class LimitePrincipal():
    def __init__(self, root, controle):
        # Aqui estamos dizendo que essa janelinha vai depender de outras coisinhas.
        self.controle = controle
        self.root = root
        # Agora, a janelinha vai ter um tamanho específico.
        self.root.geometry('300x200')
        # E terá uma barra lá no topo, com uns menus como num restaurante.
        self.menubar = tk.Menu(self.root)        

        # Vamos criar um menu chamado "Estudante". Dentro desse menu, teremos opções como "Inserir" e "Mostrar".
        self.estudanteMenu = tk.Menu(self.menubar)
        self.estudanteMenu.add_command(label="Inserir", \
                    command=self.controle.insereEstudantes)
        self.estudanteMenu.add_command(label="Mostrar", \
                    command=self.controle.mostraEstudantes)
        # Agora, adicionamos esse menu bonitinho na barra lá no topo.
        self.menubar.add_cascade(label="Estudante", \
                    menu=self.estudanteMenu)

        # Da mesma forma, vamos criar um menu para "Disciplina" com opções "Inserir" e "Mostrar".
        self.discipMenu = tk.Menu(self.menubar)
        self.discipMenu.add_command(label="Inserir", \
                    command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="Mostrar", \
                    command=self.controle.mostraDisciplinas)
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discipMenu)

        # E um menu para "Turma", mas por enquanto, sem nada dentro.
        self.turmaMenu = tk.Menu(self.menubar)
        self.turmaMenu.add_command(label="Inserir")
        self.menubar.add_cascade(label="Turma", \
                    menu=self.turmaMenu)        

        # Por fim, dizemos que a barra lá no topo pertence à nossa janelinha.
        self.root.config(menu=self.menubar)

# Agora, vamos criar o chefinho que vai controlar tudo.
class ControlePrincipal():       
    def __init__(self):
        # Aqui dizemos ao computador para criar uma janelinha.
        self.root = tk.Tk()

        # Criamos uns "chefinhos" que vão cuidar dos estudantes e das disciplinas.
        self.ctrlEstudante = est.CtrlEstudante()
        self.ctrlDisciplina = dis.CtrlDisciplina()

        # Agora, criamos uma janelinha bonita usando a classe LimitePrincipal.
        self.limite = LimitePrincipal(self.root, self) 

        # Damos um nome para a janelinha.
        self.root.title("Exemplo MVC")
        # E começamos a mostrar a janelinha para o usuário.
        self.root.mainloop()
       
    # Essas são como as ordens que o chefinho dá aos "chefinhos" dos estudantes e disciplinas.
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes()

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

# Por fim, dizemos ao computador para começar tudo, só se o código estiver sendo executado diretamente, não se estiver sendo importado.
if __name__ == '__main__':
    c = ControlePrincipal()

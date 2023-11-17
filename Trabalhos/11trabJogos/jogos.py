from tkinter import *
from tkinter import messagebox ,ttk

class JogoCadastroException(Exception):
    pass

class Jogo:
    def __init__(self, cod, titulo, console, genero, preco):
        self.__cod =cod
        self.__titulo = titulo
        self.__console = console
        self.__genero = genero
        self.__preco = preco
        self.__avaliacao = []

    @property
    def getCod(self):
        return self.__cod
    
    @property
    def getTitulo(self):
        return self.__titulo
    
    @property
    def getConsole(self):
        return self.__console
    
    @property
    def getGenero(self):
        return self.__genero
    
    @property
    def getPreco(self):
        return self.__preco
    
    def getAvaliacao(self):
        return self.__avaliacao
        
class ViewCadstroJogo(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry("500x500")
        self.title("Cadastro")
        self.controle = controle

        self.frameCod = Frame(self)
        self.frameTitulo = Frame(self)
        self.frameConsole = Frame(self)
        self.frameGenero= Frame(self)
        self.framePreco= Frame(self)
        self.frameCod.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton = Frame(self)
        self.frameButton.pack()

        self.labelCod = Label(self.frameCod, text="Cod: ")
        self.labelCod.pack(side="left")
        self.labelTitulo = Label(self.frameTitulo, text="Titulo: ")
        self.labelTitulo.pack(side="left")
        self.labelConsole = Label(self.frameConsole, text="Console: ")
        self.labelConsole.pack(side="left")
        self.labelGenero = Label(self.frameGenero, text="Genero: ")
        self.labelGenero.pack(side="left")
        self.labelPreco = Label(self.framePreco, text="Preco: ")
        self.labelPreco.pack(side="left")

        self.inputCod = Entry(self.frameCod, width=20)
        self.inputCod.pack(side="left")
        self.inputTitulo = Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        self.inputConsole = Entry(self.frameConsole, width=20)
        self.inputConsole.pack(side="left")
        self.inputGenero = Entry(self.frameGenero, width=20)
        self.inputGenero.pack(side="left")
        self.inputPreco = Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")

        self.buttonSubmit = Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastrarJogo)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewAvaliaJogo(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry("500x500")
        self.title("Avaliação")
        self.controle = controle

        self.frameCodJogoAvaliado = Frame(self)
        self.frameEstrelas = Frame(self)
        self.frameButton = Frame(self)

        self.frameCodJogoAvaliado.pack()
        self.frameEstrelas.pack() 
        self.frameButton.pack()

        self.labelCod = Label(self.frameCodJogoAvaliado, text="Cod do jogo que deseja avaliar: ")
        self.labelCod.pack(side="left")
        self.inputCodJogoAvaliado = Entry(self.frameCodJogoAvaliado, width=20)
        self.inputCodJogoAvaliado.pack(side="left")

        self.labelEstrelas = Label(self.frameEstrelas, text="Escolha o numero de estrelas: ")
        self.labelEstrelas.pack(side="left")
        self.escolhaCombo = StringVar()
        self.combobox = ttk.Combobox(self.frameEstrelas, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = [1,2,3,4,5]


        self.buttonSubmit = Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastrarAvaliacao)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewConsultaJogo(Toplevel):
    def __init__(self, controle):
        Toplevel.__init__(self)
        self.geometry("500x500")
        self.title("Consulta")
        self.controle = controle

        self.frameEstrelas = Frame(self)
        self.frameButton = Frame(self)

        self.frameEstrelas.pack() 
        self.frameButton.pack()

        self.labelEstrelas = Label(self.frameEstrelas, text="Escolha o numero de estrelas: ")
        self.labelEstrelas.pack(side="left")
        self.escolhaCombo = StringVar()
        self.combobox = ttk.Combobox(self.frameEstrelas, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = [1,2,3,4,5]


        self.buttonSubmit = Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultaJogoAvaliacao)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlJogo():
    def __init__(self ,controlePrincipal):
        self.listaJogos = []
        self.ctrlPrincipal = controlePrincipal

    def inserirJogo(self):
        self.viewCadastroJogo = ViewCadstroJogo(self)
    
    def avaliaJogo(self): 
        self.viewAvaliaJogo = ViewAvaliaJogo(self)

    def consultarJogo(self):
        self.viewConsultaJogo = ViewConsultaJogo(self)

    def cadastrarJogo(self, event):
        try:
            cod = self.viewCadastroJogo.inputCod.get()
            titulo = self.viewCadastroJogo.inputTitulo.get()
            console = self.viewCadastroJogo.inputConsole.get()
            genero = self.viewCadastroJogo.inputGenero.get()
            preco = self.viewCadastroJogo.inputPreco.get()

            # Validações usando Exceptions
            if not cod:
                raise JogoCadastroException("Código não pode ser vazio.")

            if not titulo:
                raise JogoCadastroException("Título não pode ser vazio.")

            if console not in ["XBox", "PlayStation", "Switch", "PC"]:
                raise JogoCadastroException("Console inválido.")

            if genero not in ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]:
                raise JogoCadastroException("Gênero inválido.")

            try:
                preco_float = float(preco)
                if not (0 < preco_float <= 500):
                    raise JogoCadastroException("Preço deve ser maior que zero e menor ou igual a 500.")
            except ValueError:
                raise JogoCadastroException("Preço deve ser um número válido.")

            novoJogo = Jogo(cod, titulo, console, genero, preco)
            self.listaJogos.append(novoJogo)

            self.viewCadastroJogo.mostraJanela("Cadastro", f"Jogo {titulo} cadastrado com sucesso!")

        except JogoCadastroException as e:
            self.viewCadastroJogo.mostraJanela("Erro no Cadastro", str(e))

    def cadastrarAvaliacao(self, event):
        cod = self.viewAvaliaJogo.inputCodJogoAvaliado.get()
        avaliacao = self.viewAvaliaJogo.escolhaCombo.get()

        for jogo in self.listaJogos:
            if jogo.getCod == cod:
                jogo.getAvaliacao().append(avaliacao)# coloco uma avaliaçao na lista de avaliaçoses
                break
        
        self.viewAvaliaJogo.mostraJanela("Avaliacao", f"Jogo de codigo {cod} avaliado com sucesso!")
    
    def consultaJogoAvaliacao(self, event):
        nEstrela = self.viewConsultaJogo.escolhaCombo.get()
        retorno = f"Lista de jogos:\n"
        for jogo in self.listaJogos:
            if int(self.calcMediaAvaliacao(jogo.getAvaliacao())) == int(nEstrela): #calculo a media da avaliaçao de todos os jogos quando o valor for igual ao solicitado ele printa o jogo
                retorno += f"\n\nNome: {jogo.getTitulo}\nConsole: {jogo.getConsole}\nPreço: R${jogo.getPreco}\n\n"
        
        self.viewConsultaJogo.mostraJanela(f"Jogos {nEstrela} estrelas", retorno)

    def calcMediaAvaliacao(self, lista):
        soma = 0
        cont = 0
        for nota in lista:
            soma += int(nota)
            cont += 1

        media = soma / cont

        if media <= 1 and media >= 0:
            media = 1
        
        elif media <= 2 and media > 1:
            media = 2

        elif media <= 3 and media > 2:
            media = 3

        elif media <= 4 and media > 3:
            media = 4
        
        elif media <= 5 and media > 4:
            media = 5

        else: 
            media = "Erro noa calculo..."

        return media
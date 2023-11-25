import tkinter
from tkinter import messagebox

class Cliente():
    def __init__(self, nome, endereco, email, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__email = email
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @property
    def email(self):
        return self.__email

    @property
    def cpf(self):
        return self.__cpf

class ViewCadastraCliente(tkinter.Toplevel):
    def __init__(self, controle):

        tkinter.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("400x200")
        self.title("Cadastrar cliente")

        self.frameNome = tkinter.Frame(self)
        self.frameNome.pack()
        self.frameEndereco = tkinter.Frame(self)
        self.frameEndereco.pack()
        self.frameEmail = tkinter.Frame(self)
        self.frameEmail.pack()
        self.frameCpf = tkinter.Frame(self)
        self.frameCpf.pack()
        self.frameButtons = tkinter.Frame(self)
        self.frameButtons.pack()

        self.labelNome = tkinter.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.inputNome = tkinter.Entry(self.frameNome)
        self.inputNome.pack(side="left")

        self.labelEndereco = tkinter.Label(self.frameEndereco, text="Endereço: ")
        self.labelEndereco.pack(side="left")
        self.inputEndereco = tkinter.Entry(self.frameEndereco)
        self.inputEndereco.pack(side="left")

        self.labelEmail = tkinter.Label(self.frameEmail, text="E-mail: ")
        self.labelEmail.pack(side="left")
        self.inputEmail = tkinter.Entry(self.frameEmail)
        self.inputEmail.pack(side="left")

        self.labelCpf = tkinter.Label(self.frameCpf, text="CPF: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tkinter.Entry(self.frameCpf)
        self.inputCpf.pack(side="left")

        self.buttonCadastrar = tkinter.Button(self.frameButtons, text="Cadastrar")
        self.buttonCadastrar.pack(side="left")
        self.buttonCadastrar.bind("<Button>", controle.botaoCadastrarCliente)
        self.buttonCancelar = tkinter.Button(self.frameButtons, text="Cancelar")
        self.buttonCancelar.pack(side="left")
        self.buttonCancelar.bind("<Button>", controle.botaoCancelarCliente)
        self.buttonLimpar = tkinter.Button(self.frameButtons, text="Limpar")
        self.buttonLimpar.pack(side="left")
        self.buttonLimpar.bind("<Button>", controle.botaoLimpaCliente)

    def mostraSucesso(self, titulo, msg):
            messagebox.showinfo(titulo, msg)

    def mostraErro(self, titulo, msg):
        messagebox.showerror(titulo, msg)

class ViewConsultarCliente(tkinter.Toplevel):
    def __init__(self, controle):
        tkinter.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("400x200")
        self.title("Consultar cliente")

        self.frameCpf = tkinter.Frame(self)
        self.frameCpf.pack()
        self.frameButtons = tkinter.Frame(self)
        self.frameButtons.pack()

        self.labelCpf = tkinter.Label(self.frameCpf, text="Informe o CPF: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tkinter.Entry(self.frameCpf)
        self.inputCpf.pack(side="left")
        self.buttonConsultar = tkinter.Button(self.frameButtons, text="Consultar")
        self.buttonConsultar.pack(side="left")
        self.buttonConsultar.bind("<Button>", controle.botaoConsultarCliente)
        self.buttonCancelar = tkinter.Button(self.frameButtons, text="Cancelar")
        self.buttonCancelar.pack(side="left")
        self.buttonCancelar.bind("<Button>", controle.botaoCancelarConsulta)

    def mostraSucesso(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

    def mostraErro(self, titulo, msg):
        messagebox.showerror(titulo, msg)

class CtrlCliente():
    listaClientes = [Cliente("nome", "endereco", "email", "cpf"),]
    # if not os.path.isfile("jogo.pickle"):
    #         listaJogo =  []
    # else:
    #     with open("jogo.pickle", "rb") as f:
    #         listaJogo = pickle.load(f)


    def cadastrarCliente(self):
        self.viewCliente = ViewCadastraCliente(self)

    def consultarCliente(self):
        self.viewCliente = ViewConsultarCliente(self)

    def botaoCadastrarCliente(self, event):
        nome = self.viewCliente.inputNome.get()
        endereco = self.viewCliente.inputEndereco.get()
        email = self.viewCliente.inputEmail.get()
        cpf = self.viewCliente.inputCpf.get()
        cliente = Cliente(nome, endereco, email, cpf)
        self.listaClientes.append(cliente)
        self.viewCliente.destroy()

    def botaoCancelarCliente(self, event):
        self.viewCliente.destroy()

    def botaoLimpaCliente(self, event):
        self.viewCliente.inputNome.delete(0, len(self.viewCliente.inputNome.get()))
        self.viewCliente.inputEndereco.delete(0, len(self.viewCliente.inputEndereco.get()))
        self.viewCliente.inputEmail.delete(0, len(self.viewCliente.inputEmail.get()))
        self.viewCliente.inputCpf.delete(0, len(self.viewCliente.inputCpf.get()))

    def botaoConsultarCliente(self, event):
        cpf = self.viewCliente.inputCpf.get()
        msg = ""
        for cliente in self.listaClientes:
            if cliente.cpf == cpf:
                msg = "Nome: " + cliente.nome + "\n" + "Endereço: " + cliente.endereco
                msg += "\n" + "Email: " + cliente.email + "\n" + "CPF: " + cliente.cpf
                self.viewCliente.mostraSucesso("Cliente encontrado", msg)
                break
        else:
            self.viewCliente.mostraErro("Cliente não encontrado", "Cliente não existe no sistema ou não foi cadastrado")

    def botaoCancelarConsulta(self, event):
        self.viewCliente.destroy()


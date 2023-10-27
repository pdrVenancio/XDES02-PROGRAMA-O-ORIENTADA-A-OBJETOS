#Nome: Pedro Venancio dos Santos Matricula: 2023010066

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email
    
    @property
    def codigo(self):
        return self.__codigo

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        #texto
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Codigo: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")
        self.labelInfo3.pack(side="left") 

        #campo para digitar
        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")               
      
        #botoes
        self.buttonSubmit = tk.Button(self.janela,text="Salva")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Limpa")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)    

        self.buttonShow = tk.Button(self.janela,text="Mostrar lista de clientes",)
        self.buttonShow.pack(side="left")
        self.buttonShow.bind("<Button>", controller.MostraHandler)         

        self.buttonSearch = tk.Button(self.janela,text="Consultar Clientes")
        self.buttonSearch.pack(side="left")
        self.buttonSearch.bind("<Button>", controller.ConsultaCod)   

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x100')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def salvaHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        codigoCli = self.view.inputText3.get()
        cliente = ModelCliente(nomeCli, emailCli, codigoCli)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get())) 
        self.view.inputText3.delete(0, len(self.view.inputText3.get())) 
        
    
    def MostraHandler(self, event):
        msg = "Clientes cadastrados:\n"
        for cliente in self.listaClientes:
            msg += cliente.nome + " - " + cliente.email + " - " +  cliente.codigo + "\n"
        
        self.view.mostraJanela("Lista de clientes", msg)
    
    def ConsultaCod(self, event):
        cont = 0
        answer = simpledialog.askstring("Consultar clientes", "Qual o codigo??",
                                            parent=self.view.janela)
    

        for cliente in self.listaClientes:
            if answer == str(cliente.codigo):
                clienteCerto = cliente 
                cont = 1

        if cont == 1:
            msg = f"Cliente de codigo {answer}:\n"
            msg += clienteCerto.nome + " - " + clienteCerto.email + " - " +  clienteCerto.codigo + "\n"
            self.view.mostraJanela("CLIENTE ENCONTRADO!!!!!!!!", msg)
        else:
            self.view.mostraJanela("",f"Cliente nao cadastrado! {answer}")
        

if __name__ == '__main__':
    c = Controller()
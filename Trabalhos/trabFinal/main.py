# TRABALHO FINAL - sistema para gerenciamento de vendas de um açougue

# ==============================
# Breno Vieira Nogueira Carneiro
# Matrícula: 2023003929
#
# Pedro Venâncio dos Santos
# Matrícula: 2023010066
# ==============================

import tkinter
import cliente
import produto
import notaFiscal


class LimitePrincipal():

    def __init__(self, root, controle):
        self.root = root
        self.controle = controle

        self.menubar = tkinter.Menu(self.root)
        self.menuCliente = tkinter.Menu(self.menubar, tearoff=0)
        self.menuProduto = tkinter.Menu(self.menubar, tearoff=0)
        self.menuNota = tkinter.Menu(self.menubar, tearoff=0)
        self.menuFaturamento = tkinter.Menu(self.menubar, tearoff=0)
        self.menuSair = tkinter.Menu(self.menubar, tearoff=0)

        self.menuCliente.add_command(label='Cadastrar cliente', command=self.controle.cadastrarCliente)
        self.menuCliente.add_command(label='Consultar cliente', command=self.controle.consultarCliente)
        self.menuCliente.add_command(label="Mostrar clientes cadastrados (EXTRA)", command=self.controle.mostraClientesCadastrados)
        self.menuCliente.add_command(label="Salvar", command=self.controle.salvaClientes)

        self.menubar.add_cascade(label='Cliente', menu=self.menuCliente)

        self.menuProduto.add_command(label='Cadastrar produto', command=self.controle.cadastraProduto)
        self.menuProduto.add_command(label='Remover produto', command=self.controle.removeProduto)
        self.menuProduto.add_command(label='Alterar produto', command=self.controle.alteraProduto)
        self.menuProduto.add_command(label='Consulta produto', command=self.controle.consultaProduto)
        self.menuProduto.add_command(label="Mostrar produtos cadastrados (EXTRA)", command=self.controle.mostraProdutosCadastrados)
        self.menuProduto.add_command(label="Salvar", command=self.controle.salvaProdutos)
        self.menubar.add_cascade(label='Produto', menu=self.menuProduto)

        self.menuFaturamento.add_command(label='Faturamento Produto', command=self.controle.fatProduto)
        self.menuFaturamento.add_command(label='Faturamento Cliente', command=self.controle.fatCliente)
        self.menuFaturamento.add_command(label='Faturamento por periodo', command=self.controle.fatPeriodo)
        self.menuFaturamento.add_command(label='Faturamento de um cliente em um periodo', command=self.controle.fatPeriodoCliente)
        self.menubar.add_cascade(label='Faturamento', menu=self.menuFaturamento)

        self.menuNota.add_command(label='Emitir nota', command=self.controle.emitirNota)
        self.menuNota.add_command(label='Exibir nota',command=self.controle.exibirNota)
        self.menuNota.add_command(label='Top 5 produtos', command=self.controle.rankProdutos)
        self.menuNota.add_command(label="Exibir notas emitidas (Extra)", command=self.controle.exibirNotasEmitidas)
        self.menuNota.add_command(label="Salvar", command=self.controle.salvaNotas)
        self.menubar.add_cascade(label='Nota', menu=self.menuNota)

        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        self.root.title("Vendas do açougue")

        self.ctrlProduto = produto.CtrlProduto(self)
        self.ctrlCliente = cliente.CtrlCliente()
        self.ctrlNota = notaFiscal.CtrlNotaFiscal(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.mainloop()

    #CLIENTE
    def cadastrarCliente(self):
        self.ctrlCliente.cadastrarCliente()
    def consultarCliente(self):
        self.ctrlCliente.consultarCliente()
    def mostraClientesCadastrados(self):
        self.ctrlCliente.mostraClientesCadastrados()

    #PRODUTOS
    def cadastraProduto(self):
        self.ctrlProduto.cadastraProduto()
    def removeProduto(self):
        self.ctrlProduto.removeProduto()
    def alteraProduto(self):
        self.ctrlProduto.alteraProduto()
    def consultaProduto(self):
      self.ctrlProduto.consultaProduto()
    def mostraProdutosCadastrados(self):
        self.ctrlProduto.mostraProdutosCadastrados()

    #NOTA FISCAL
    def emitirNota(self):
        self.ctrlNota.emitirNota()

    def exibirNota(self):
        self.ctrlNota.exibirNota()

    def rankProdutos(self):
        self.ctrlNota.produtosMaisVendidos()

    def exibirNotasEmitidas(self):
        self.ctrlNota.exibirNotasEmitidas()

    #FATURAMENTO
    def fatProduto(self):
        self.ctrlNota.fatProduto()

    def fatCliente(self):
        self.ctrlNota.fatCliente()

    def fatPeriodo(self):
        self.ctrlNota.fatPeriodo()

    def fatPeriodoCliente(self):
        self.ctrlNota.fatPeriodoCliente()

    def salvaProdutos(self):
        self.ctrlProduto.salvaProduto()
        self.root.destroy()

    def salvaClientes(self):
        self.ctrlCliente.salvaCliente()
        self.root.destroy()

    def salvaNotas(self):
        self.ctrlNota.salvaNota()
        self.root.destroy()

if __name__ == "__main__":
    c = ControlePrincipal()

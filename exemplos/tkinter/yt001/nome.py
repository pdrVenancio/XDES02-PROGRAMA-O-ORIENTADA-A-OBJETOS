from tkinter import *

def mostrarNome():
    nome = textbox.get()
    label_final = Label(root, text=f"seu nome é {nome}")
    label_final.grid()

root = Tk()
root.title("Nome")
root.geometry("500x500")

label = Label(root, text="Escreva o seu nome")
textbox = Entry(root)
botao = Button(root, text="Execitar", command=mostrarNome)

label.grid()
textbox.grid()
botao.grid()

root.mainloop()
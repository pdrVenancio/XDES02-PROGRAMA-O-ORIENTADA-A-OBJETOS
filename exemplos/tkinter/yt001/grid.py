from tkinter import *

menu = Tk()
menu.title("Login")

Label(menu, text="Usuario: ").grid(row=0, sticky=W)  #sticky semelhante a anchor
Label(menu, text="Senha: ").grid(row=1, sticky=W)

#textbox
textBox1 = Entry(menu).grid(row=0, column=1)
textBox2 = Entry(menu).grid(row=1, column=1)

cmd_login = Button(menu, text="Login").grid(row=2, column=1, sticky=E)

#GRID
# columnspan = valor - quantas colunas ele vai ocupar
# sticky = N W E S - posição

menu.mainloop()
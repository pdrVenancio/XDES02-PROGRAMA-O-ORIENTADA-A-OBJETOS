from tkinter import *

root = Tk()

menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Abrir")
file_menu.add_command(label="Salvar")
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)
menubar.add_cascade(label="Arquivo", menu=file_menu)

root.config(menu=menubar)
root.mainloop()

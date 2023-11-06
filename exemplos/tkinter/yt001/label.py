from tkinter import *

menu = Tk()
menu.title("lable")
menu.geometry("500x500")

label1 = Label(menu, text="Esse é o label 1")
label1.pack(side='top')

label2 = Label(menu, text="Esse é o label 2")
label2.pack(side='left')

label3 = Label(menu, text="com o\nconsigo saltar uma linha no texto")
label3.pack(side='right')

# bg="color" - cor do fundo
# fg="color" - cor da font
# font="nome tamanho variaçoes(italic, bold)" - estilo da fonte
# width / heigth


menu.mainloop()
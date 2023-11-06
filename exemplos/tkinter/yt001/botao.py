from tkinter import *

menu = Tk()
menu.title("Botao")
menu.geometry("500x500") #define a dimençao base da tela

#botao
def cmd_click(mensagem):
    print(mensagem)
    
cmd = Button(menu, text="exec 1", command=lambda:cmd_click("ola soi francisco"))#lambda par passarmos parametros para as funcos
cmd.pack()

cmd2 = Button(menu, text="exec 2", command=lambda:cmd_click("ola soi chico"))
cmd2.pack()

menu.mainloop()
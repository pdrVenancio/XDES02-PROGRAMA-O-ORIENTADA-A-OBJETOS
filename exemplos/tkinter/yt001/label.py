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
# Ao inves de pack podemos usar grid(row = 0, column = 0) - Assim usamos a tale como se fosse uma tabela/matriz

# LABEL 
#-------------------------------------------------------------------------------#
# bg ="color" - cor do fundo                                                    #
# fg ="color" - cor da font                                                     #
# font ="nome tamanho variaçoes(italic, bold)" - estilo da fonte                #
# width / heigth                                                                #
# bd = espessura - borda                                                        #
# realief = "tipo de linha da borda"                                            #
# anchor = letra do ponto cardinal maiuscula - alinhar o texto dentro do label  #
# padx / pady = valor                                                           #
# justify = CENTER, RIGHT, LEFT - justifica o alinhamento do texto              #
# textvariable = variavel - para usarmos o texto contido dentro de uma variavel #
#-------------------------------------------------------------------------------#

# PACK

menu.mainloop()
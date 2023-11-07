from tkinter import *

def converter():
    f = float(entrada_temperatura.get())
    c = (f - 32) * 5/9
    resultado.set(f"{c:.2f} graus Celsius") 

root = Tk()
root.title("Conversor de Temperatura")
resultado = StringVar()

label_texto = Label(root, text="Digite a temperatura em Fahrenheit: ")
label_texto.grid(row=0, column=0)

entrada_temperatura = Entry(root)
entrada_temperatura.grid(row=1, column=0)

botao_converter = Button(root, text="Converter", command=converter)
botao_converter.grid(row=2, column=0, columnspan=2) 

label_resultado = Label(root, textvariable=resultado)
label_resultado.grid(row=3, column=0, columnspan=2) 

root.mainloop()

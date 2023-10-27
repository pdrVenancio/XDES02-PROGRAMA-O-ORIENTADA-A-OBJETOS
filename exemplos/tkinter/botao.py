import tkinter as tk

root = tk.Tk()

# Crie um botão com padding interno
my_button = tk.Button(root, text="Clique em mim", padx=10, pady=5)
my_button.pack()


# padding externo com botoes precisamos dar padding no lreme onde ele esta inserido
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()
my_button = tk.Button(frame, text="Clique em mim")
my_button.pack()



root.mainloop()
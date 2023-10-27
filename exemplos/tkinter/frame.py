from tkinter import *

root = Tk()
root.title("Exemplo de Frame")

frame = Frame(root, borderwidth=2, relief="sunken", bg="blue")

frame.pack(fill="both", expand=True, side="top", padx=10, pady=10)

label = Label(frame, text="Este é um frame!")
label.pack(pady=10)


frame2 = Frame(root, borderwidth=2, relief="sunken", bg="green")
frame2.pack(fill="both", expand=True, side="left", padx=10, pady=10)

label = Label(frame2, text="Este é um frame2!")
label.pack(pady=10)


root.mainloop()
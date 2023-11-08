from tkinter import *

class FrameNome(Frame):
    def __init__(self, master):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self, text="Nome" )
        text_nome = Entry(self)

        label_nome.grid()
        text_nome.grid()

#########################################################################################

root = Tk()
root.title("Classes")

frame_1 = FrameNome(root)
frame_1.grid()

root.mainloop()
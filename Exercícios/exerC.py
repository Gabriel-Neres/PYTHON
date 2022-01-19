from tkinter import *

def salvar():
    pass

def carregar():
    pass

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

mainmenu = Menu(frame)
mainmenu.add_command(label="salvar", command=salvar)
mainmenu.add_command(label="carregar", command=carregar)
mainmenu.add_command(label="sair", command=root.destroy)

root.config(menu=mainmenu)

root.mainloop()
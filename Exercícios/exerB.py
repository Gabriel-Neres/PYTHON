from tkinter import *

root = Tk()
root.geometry("")
frame = Frame(root)
frame.pack()

entryName = Entry(frame, width=20)
entryName.insert(0,'usuario')
entryName.pack(padx=5, pady=5)

entrySenha = Entry(frame, width=20)
entrySenha.insert(0, 'Senha')
entrySenha.pack(padx=5, pady=5)

root.mainloop()
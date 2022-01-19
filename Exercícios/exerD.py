from tkinter import *

janela = Tk()
janela.geometry("200x200")
frame = Frame(janela)
frame.pack()

escala = Scale(frame, from_=0, to=10)
escala.pack(padx=5, pady=5)

escala2 = Scale(frame, from_=0, to=10, orient=HORIZONTAL)
escala2.pack(padx=5, pady=5)

janela.mainloop()
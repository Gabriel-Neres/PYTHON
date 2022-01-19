from tkinter import *
from tkinter import ttk

janela = Tk()
janela.geometry("200x200")
frame=Frame (janela)
frame.pack()

listatime = ["Flamengo","Vasco","Fluminense","Botafogo"]
combotime = ttk.Combobox(frame, value=listatime)
combotime.set("Escolha o time:")

itens = StringVar()
itens.set("Escolha seu time ")
times = OptionMenu(janela, itens, "Flamengo","Vasco", "Fluminense", "Botafogo")

times.pack()
combotime.pack()

janela.mainloop()
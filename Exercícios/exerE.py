from tkinter import *

janela = Tk()
janela.geometry("200x200")
frame=Frame (janela)
frame.pack()

menubttn = Menubutton(frame, text="Lista de compras", relief=RAISED)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

menu1 = Menu(menubttn, tearoff=0)

menu1.add_checkbutton(label="Tomate", variable=var1)
menu1.add_checkbutton(label="Costela de Porco", variable=var2)
menu1.add_checkbutton(label="Arroz", variable=var3)
menu1.add_checkbutton(label="Cebola", variable=var4)
menu1.add_checkbutton(label="Feijão", variable=var5)

menubttn["menu"] = menu1
menubttn.pack()
janela.mainloop()

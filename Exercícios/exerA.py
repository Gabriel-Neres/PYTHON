from tkinter import *

root =Tk()
root.geometry("200x150")#tamanho
frame = Frame(root)
frame.pack()

frameesquerda = Frame(root)
frameesquerda.pack(side=LEFT)

framedireita= Frame(root)
framedireita.pack(side=RIGHT)

label = Label(frame, text = "Exercício tk widget 1")
label.pack()

button1 = Button(frameesquerda, text="Botão 1")
button1.pack(padx=3, pady=3)
button2 = Button(framedireita, text="Botão 2")
button2.pack(padx=3, pady=3)
button3 = Button(frameesquerda, text="Botão 2")
button3.pack(padx=3, pady=3)

root.title('Exercicio A')
root.mainloop()
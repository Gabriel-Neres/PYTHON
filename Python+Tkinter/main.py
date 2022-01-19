from tkinter import *
#variaveis
cor = ["#008", "#fff", "#000"]

app = Tk()
app.title("CFB Cursos")
app.geometry("300x300")
app.configure(background=cor[0])  #

txt1 = Label(app, text="Curso de Python", background=cor[0],foreground=cor[1])  #"master, cnf"

txt1.place(x=10, y=10, width=125, height=20)  #place - insere o elemento
tx2 = "Módulo tkinter"
txt2 = Label(app, text=tx2, bg=cor[1], fg=cor[2])
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side="top", fill=X,
          expand=True)  #ipad - interno, pad vertical,x=horizontal e y=vertical
#fill expasamento
#expande - se True ou False

app.mainloop()  #roda o programa
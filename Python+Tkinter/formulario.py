from tkinter import *
import os

c=os.path.dirname(__file__)
nomeArquivo=c+"\\Contas.txt"

def gravarDados():
    arquivo= open(nomeArquivo, "a+")
    arquivo.write("Nome:%s" % innome.get())
    arquivo.write("\nTelefone:%s" % intelefone.get())
    arquivo.write("\nEmail:%s" % inemail.get())
    arquivo.write("\nObs:%s" % inobs.get("1.0",END))
    arquivo.write("\n")
    arquivo.close()

app = Tk()
app.title("Aula 2 Tkinter")
app.geometry("600x600")
app.configure(background="#dde")

#anchor=> N=Norte,S=Sul,E=Leste e W=Oeste
#SE = Sudeste, SO = Sudoeste
Label(app, text="Nome", bg="#dde",fg="#009", anchor=W).place(x=10,y=10,width=100,height=20)
innome= Entry(app)
innome.place(x=10,y=40,width=200, height=20)

Label(app, text="Telefone", bg="#dde",fg="#009", anchor=W).place(x=10,y=70,width=100,height=20)
intelefone = Entry(app)
intelefone.place(x=10,y=100,width=100, height=20)

Label(app, text="E-mail", bg="#dde",fg="#009", anchor=W).place(x=10,y=130,width=100,height=20)
inemail = Entry(app)
inemail.place(x=10,y=160,width=200, height=20)

Label(app, text="OBS", bg="#dde",fg="#009", anchor=W).place(x=10,y=180,width=100,height=20)
inobs = Text(app)
inobs.place(x=10,y=200,width=200, height=80)

Button(app, text="Gravar", command=gravarDados).place(x=10, y=300)
app.mainloop()
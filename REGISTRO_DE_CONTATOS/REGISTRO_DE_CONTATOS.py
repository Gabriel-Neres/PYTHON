import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3

# --------- FRAMES - PRINCIPAL -------------
root = Tk()
root.title("**** LISTA DE CONTATOS *****")
width = 700
height = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0,0)

root.config(bg='#6666ff')

# --------- VARIAVEIS -------------

nome = StringVar()
telefone = StringVar()
idade = StringVar()
email = StringVar()
endereco = StringVar()
id = None
updateWindow = None
newWindow = None

# --------- METODOS -------------


def database():
    conn = sqlite3.connect("contatos.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'humanos' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT, telefone TEXT, idade TEXT, email TEXT, endereco TEXT) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'humanos' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def submitData():
    if nome.get() == "" or telefone.get() == "" or idade.get() == "" or email.get() == "" or endereco.get() == "":
        resultado = msb.showwarning(
            "", "Por favor, digite todos os campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contatos.db")
        cursor = conn.cursor()
        query = """ INSERT INTO 'humanos' (nome, telefone, idade, email, endereco) VALUES(?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(telefone.get()), str(
            idade.get()), str(email.get()), str(endereco.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'humanos' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        telefone.set("")
        idade.set("")
        email.set("")
        endereco.set("")


def updateData():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("contatos.db")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE 'humanos' SET nome = ?, telefone = ?, idade = ?, email = ?, endereco = ? WHERE id = ?""",
                   (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get()), int(id)))    
    conn.commit()
    cursor.execute("SELECT * FROM 'humanos' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    updateWindow.destroy()

def onSelect(event):
    global id, updateWindow
    selectItem = tree.focus()
    conteudo = (tree.item(selectItem))
    selectedItem = conteudo['values']
    id = selectedItem[0]
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    nome.set(selectedItem[1])
    telefone.set(selectedItem[2])
    idade.set(selectedItem[3])
    email.set(selectedItem[4])
    endereco.set(selectedItem[5])
    # --------- FRAMES - ATUALIZAR -------------
    updateWindow = Toplevel()
    updateWindow.title("**** ATUALIZANDO CONTATO *****")
    formTitulo = Frame(updateWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(updateWindow)
    formContato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = updateWindow.winfo_screenwidth()
    sc_height = updateWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    updateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    updateWindow.resizable(0, 0)

    # --------- LABELS - ATUALIZAR -------------
    lbl_title = Label(formTitulo, text="Atualizando contatos",
                      font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(formContato, text='Telefone', font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(formContato, text='Idade', font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(formContato, text='Email', font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(formContato, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)

    # --------- ENTRY - ATUALIZAR -------------
    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    telefoneEntry = Entry(formContato, textvariable=telefone, font=('arial', 12))
    telefoneEntry.grid(row=1, column=1)
    idadeEntry = Entry(formContato, textvariable=idade, font=('arial', 12))
    idadeEntry.grid(row=2, column=1)
    emailEntry = Entry(formContato, textvariable=email, font=('arial', 12))
    emailEntry.grid(row=3, column=1)
    enderecoEntry = Entry(formContato, textvariable=endereco, font=('arial', 12))
    enderecoEntry.grid(row=4, column=1)
    # --------- BOTÃO - ATUALIZAR -------------
    bttn_updatecom = Button(formContato, text="Atualizar",
                            width=50, command=updateData)
    bttn_updatecom.grid(row=6, columnspan=2, pady=10)


# --------- METODO - DELETAR -------------
def deleteData():
    if not tree.selection():
        resultado = msb.showwarning(
            '', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion(
            '', 'Tem certeza que deseja deletar o contato?')
        if resultado == 'yes':
            selectItem = tree.focus()
            conteudo = (tree.item(selectItem))
            selectedItem = conteudo['values']
            tree.delete(selectItem)
            conn = sqlite3.connect("contatos.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM 'humanos' WHERE id = %d" %
                           selectedItem[0])
            conn.commit()
            cursor.close()
            conn.close()


def insertData():
    global newWindow
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    # --------- FRAMES - CADASTRAR -------------
    newWindow = Toplevel()
    newWindow.title("**** INSERINDO CONTATO *****")
    formTitulo = Frame(newWindow)
    formTitulo.pack(side=TOP)
    formContato = Frame(newWindow)
    formContato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = newWindow.winfo_screenwidth()
    sc_height = newWindow.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    newWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    newWindow.resizable(0, 0)

    # --------- LABELS - CADASTRAR -------------
    lbl_title = Label(formTitulo, text="Inserindo contatos",
                      font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContato, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(formContato, text='Telefone', font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(formContato, text='Idade', font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(formContato, text='Email', font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(formContato, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)

    # --------- ENTRY - CADASTRAR -------------
    nomeEntry = Entry(formContato, textvariable=nome, font=('arial', 12))
    nomeEntry.grid(row=0, column=1)
    telefoneEntry = Entry(
        formContato, textvariable=telefone, font=('arial', 12))
    telefoneEntry.grid(row=1, column=1)
    idadeEntry = Entry(formContato, textvariable=idade, font=('arial', 12))
    idadeEntry.grid(row=2, column=1)
    emailEntry = Entry(formContato, textvariable=email, font=('arial', 12))
    emailEntry.grid(row=3, column=1)
    enderecoEntry = Entry(
        formContato, textvariable=endereco, font=('arial', 12))
    enderecoEntry.grid(row=4, column=1)
    # --------- BOTÃO - CADASTRAR -------------
    bttn_submitcom = Button(formContato, text="Cadastrar",
                            width=50, command=submitData)
    bttn_submitcom.grid(row=6, columnspan=2, pady=10)


# ---------------- FRAME PRINCIPAL -------------
top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg='#6666ff')
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=10)
midleftPadding = Frame(mid, width=350, bg="#6666ff")
midleftPadding.pack(side=LEFT)
midright = Frame(mid, width=100)
midright.pack(side=RIGHT, pady=10)
bottom = Frame(root, width=500)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

# --------------- LABELS PRINCIPAL --------------
lbl_title = Label(top, text="SISTEMA DE GERENCIAMENTO DE CONTATOS", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alterar = Label(bottom, text="Para alterar clique duas vezes no contato desejado.", font=('arial', 12), width=200)
lbl_alterar.pack(fill=X)

# --------------- BUTTONS PRINCIPAL --------------
bttn_add = Button(midleft, text="INSERIR", bg="royal blue", command=insertData)
bttn_add.pack()
bttn_delete = Button(midright, text="Deletar",
                     bg="OrangeRed2", command=deleteData)
bttn_delete.pack(side=RIGHT)
# --------------- TREEVIEW PRINCIPAL --------------

ScrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Nome", "Telefone", "Idade", "Email", "Endereço"),
                    height=400, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand = ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Telefone", text="Telefone", anchor=W)
tree.heading("Idade", text="Idade", anchor=W)
tree.heading("Email", text="Email", anchor=W)
tree.heading("Endereço", text="Endereço", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', onSelect)

# --------- MENU - PRINCIPAL ---------------
menu_bar = Menu(root)
root.config(menu=menu_bar)

# adicionar itens
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Criar novo", command=insertData)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.destroy)

menuSobre = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Sobre", menu=menuSobre)
menuSobre.add_command(label="Info")


if __name__ == '__main__':
    database()
    root.mainloop()

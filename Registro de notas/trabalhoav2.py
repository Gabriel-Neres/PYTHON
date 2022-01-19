import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import *
import sqlite3

window = Tk()
window.title("REGISTRO DE NOTAS PESSOAIS")
window.configure(background='#483d8b')
window.geometry("700x600")
window.resizable(True, False)
window.minsize(width=700, height=600)
window.minsize(width=900, height=600)

id_entry = StringVar()
disciplina_entry = StringVar()
av1_entry = StringVar()
av2_entry = StringVar()
av3_entry = StringVar()
avd_entry = StringVar()
avds_entry = StringVar()
status = StringVar()
media = StringVar()

#FUNÇOES
def create_db():
    conn = sqlite3.connect("reg_notas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS 'notas' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, disciplina TEXT, av1 FLOAT, av2 FLOAT, av3 FLOAT, avd FLOAT, avds FLOAT, media FLOAT, status TEXT) """
    )
    conn.commit()
    print("Banco de dados criado.")
    conn.close()

def insert_record():
    id_entry = ent_id.get()
    disciplina_entry = ent_disciplina.get()
    av1_entry = ent_av1.get()
    av2_entry = ent_av2.get()
    av3_entry = ent_av3.get()
    avd_entry = ent_avd.get()
    avds_entry = ent_avds.get()
    status = StringVar()
    try:
        if disciplina_entry == "" or av1_entry == "" or av2_entry == "" or avd_entry == "":
            resultado = msb.showwarning("",
                                        "Digite em todos os campos!",
                                        icon="warning")
        else:
            media = (float(av1_entry) + float(av2_entry) +
                     float(avd_entry)) / 3
            if media >= 60:
                status = "Aprovado"
            else:
                status = "Reprovado"

            conn = sqlite3.connect("reg_notas.db")
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO 'notas' (disciplina, av1, av2, av3, avd, avds, media, status) VALUES(?,?,?,?,?,?,?, ?)""",
                (disciplina_entry, av1_entry, av2_entry, av3_entry, avd_entry,
                 avds_entry, media, status))
            conn.commit()
            conn.close()
            onSelect()
            clean_screen
    except ValueError:
        result = msb.showwarning("", "Digite o valor certo!", icon="warning")

def delete_record():
    id_entry = ent_id.get()
    disciplina_entry = ent_disciplina.get()
    av1_entry = ent_av1.get()
    av2_entry = ent_av2.get()
    av3_entry = ent_av3.get()
    avd_entry = ent_avd.get()
    avds_entry = ent_avds.get()
    try:
        if not list_record.selection():
            result = msb.showwarning('',
                                     'Por favor, selecione o item na lista.',
                                     icon='warning')
        else:
            result = msb.askquestion(
                '', 'Tem certeza que deseja deletar o registro?')
            if result == 'yes':
                conn = sqlite3.connect("reg_notas.db")
                cursor = conn.cursor()
                cursor.execute("""DELETE FROM notas WHERE id = ?""",
                               (id_entry, ))
                conn.commit()
                conn.close()
                clean_screen()
                onSelect()
    except sqlite3.Error as error:
        resul = msb.showwarning("",
                                "Falha ao excluir registro",
                                icon="warning")

def update_record():
    id_entry = ent_id.get()
    disciplina_entry = ent_disciplina.get()
    av1_entry = ent_av1.get()
    av2_entry = ent_av2.get()
    av3_entry = ent_av3.get()
    avd_entry = ent_avd.get()
    avds_entry = ent_avds.get()
    try:
        if not list_record.selection():
            result = msb.showwarning('',
                                     'Por favor, selecione o item na lista.',
                                     icon='warning')
        else:
            result = msb.askquestion(
                '', 'Tem certeza que deseja editar o registro?')
        if result == 'yes':
                media = (float(av1_entry) + float(av2_entry) + float(avd_entry)) / 3
                if media >= 60:
                        status = "Aprovado"
                else:
                        status = "Reprovado"

                conn = sqlite3.connect("reg_notas.db")
                cursor = conn.cursor()
                cursor.execute(
                """ UPDATE 'notas' SET disciplina = ?, av1 = ?, av2 = ?, av3 = ?, avd = ?, avds=? , media = ? , status = ? WHERE id = ?""",
                (disciplina_entry, av1_entry, av2_entry, av3_entry, avd_entry,
                avds_entry, media, status, id_entry))
                conn.commit()
                conn.close()
                onSelect()
                clean_screen()
    except sqlite3.Error as error:
        resultado = msb.showwarning("",
                                    "Falha ao alterar registro",
                                    icon="warning")

def update2():
    id_entry = ent_id.get()
    disciplina_entry = ent_disciplina.get()
    av1_entry = ent_av1.get()
    av2_entry = ent_av2.get()
    av3_entry = ent_av3.get()
    avd_entry = ent_avd.get()
    avds_entry = ent_avds.get()
    try:
        if not list_record.selection():
            result = msb.showwarning('',
                                     'Por favor, selecione o item na lista.',
                                     icon='warning')
        else:
            if float(av3_entry) > float(av1_entry) or float(av2_entry):
                if float(av1_entry) > float(av2_entry) or float(
                        av1_entry) == float(av2_entry):
                    av2_entry = av3_entry
                else:
                    av1_entry = av3_entry

                    media = (float(av1_entry) + float(av2_entry) +
                            float(avd_entry)) / 3
                    if media >= 60:
                        status = "Aprovado"
                    else:
                        status = "Reprovado"

                    conn = sqlite3.connect("reg_notas.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        """ UPDATE 'notas' SET disciplina = ?, av1 = ?, av2 = ?, av3 = ?, avd = ?, avds=? , media = ? , status = ? WHERE id = ?""",
                        (disciplina_entry, av1_entry, av2_entry, av3_entry, avd_entry,
                        avds_entry, media, status, id_entry))
                    conn.commit()
                    conn.close()
                    onSelect()
                    clean_screen()
    except sqlite3.Error as error:
        resultado = msb.showwarning("",
                                        "Falha ao alterar registro",
                                        icon="warning")
    
def update3():
    id_entry = ent_id.get()
    disciplina_entry = ent_disciplina.get()
    av1_entry = ent_av1.get()
    av2_entry = ent_av2.get()
    av3_entry = ent_av3.get()
    avd_entry = ent_avd.get()
    avds_entry = ent_avds.get()
    try:
        if not list_record.selection():
            result = msb.showwarning('',
                                     'Por favor, selecione o item na lista.',
                                     icon='warning')
        else:
            if float(avds_entry) > float(avd_entry):
                avd_entry = avds_entry

                media = (float(av1_entry) + float(av2_entry) +
                        float(avd_entry)) / 3
                if media >= 60:
                    status = "Aprovado"
                else:
                    status = "Reprovado"

                conn = sqlite3.connect("reg_notas.db")
                cursor = conn.cursor()
                cursor.execute(
                    """ UPDATE 'notas' SET disciplina = ?, av1 = ?, av2 = ?, av3 = ?, avd = ?, avds=? , media = ? , status = ? WHERE id = ?""",
                    (disciplina_entry, av1_entry, av2_entry, av3_entry, avd_entry,
                    avds_entry, media, status, id_entry))
                conn.commit()
                conn.close()
                onSelect()
                clean_screen()
    except sqlite3.Error as error:
        resultado = msb.showwarning("","Falha ao alterar registro",
                                        icon="warning")
    
def clean_screen():
    ent_id.delete(0, END)
    ent_disciplina.delete(0, END)
    ent_av1.delete(0, END)
    ent_av2.delete(0, END)
    ent_av3.delete(0, END)
    ent_avd.delete(0, END)
    ent_avds.delete(0, END)

def onDuploClick(event):
    clean_screen()
    list_record.selection()

    for i in list_record.selection():
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = list_record.item(
            i, 'values')
        ent_id.insert(END, col1)
        ent_disciplina.insert(END, col2)
        ent_av1.insert(END, col3)
        ent_av2.insert(END, col4)
        ent_av3.insert(END, col5)
        ent_avd.insert(END, col6)
        ent_avds.insert(END, col7)
        media.insert(END, col8)
        status.insert(END, col9)

def onSelect():
    list_record.delete(*list_record.get_children())
    conn = sqlite3.connect("reg_notas.db")
    cursor = conn.cursor()
    lista = cursor.execute(
        """SELECT id, disciplina, av1, av2, av3, avd, avds, media, status FROM notas ORDER BY id"""
    )
    for i in lista:
        list_record.insert("", END, values=i)
    conn.close()

def search_record():
    conn = sqlite3.connect("reg_notas.db")
    cursor = conn.cursor()
    list_record.delete(*list_record.get_children())
    ent_disciplina.insert(END, '%')
    disc = ent_disciplina.get()
    cursor.execute(
        """SELECT id, disciplina, av1, av2, av3, avd, avds, media, status FROM notas WHERE disciplina LIKE '%s' ORDER BY disciplina ASC"""
        % disc)
    search_disc = cursor.fetchall()
    for i in search_disc:
        list_record.insert("", END, values=i)
    clean_screen()
    conn.close()

#FRAME MENU
frameMenu = Frame(window, bg="#fffaf0")
frameMenu.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)

#BOTÕES
bt_enviar = Button(frameMenu,text="ENVIAR",bg='#483d8b',foreground="#fffaf0",bd=3,command=insert_record)
bt_enviar.place(relx=0.84, rely=0.09, relheight=0.15, relwidth=0.15)
bt_editar = Button(frameMenu,text="EDITAR",bg='#483d8b',foreground="#fffaf0",bd=3,command=update_record)
bt_editar.place(relx=0.84, rely=0.25, relheight=0.15, relwidth=0.15)
bt_excluir = Button(frameMenu,text="EXCLUIR",bg='#483d8b',foreground="#fffaf0",bd=3,command=delete_record)
bt_excluir.place(relx=0.84, rely=0.41, relheight=0.15, relwidth=0.15)
bt_limpar = Button(frameMenu,text="LIMPAR",bg='#483d8b',foreground="#fffaf0",bd=3,command=clean_screen)
bt_limpar.place(relx=0.84, rely=0.57, relheight=0.15, relwidth=0.15)
bt_buscar = Button(frameMenu,text="BUSCAR",bg='#483d8b',foreground="#fffaf0",bd=3,command=search_record)
bt_buscar.place(relx=0.84, rely=0.73, relheight=0.15, relwidth=0.15)
bt_update2 = Button(frameMenu,text="Altere sua AV1 e AV2 com sua da notas da AV3",bg='#483d8b',foreground="#fffaf0",bd=3,command=update2)
bt_update2.place(relx=0.24, rely=0.55, relheight=0.15, relwidth=0.47)
bt_update2 = Button(frameMenu,text="Altere sua AVD com sua da nota da AVDS",bg='#483d8b',foreground="#fffaf0",bd=3,command=update3)
bt_update2.place(relx=0.24, rely=0.75, relheight=0.15, relwidth=0.47)

#LABEL&ENTRY
lb_id = Label(frameMenu,text="ID",bg="#fffaf0",font=('Helvetica', 11, 'bold'))
lb_id.place(relx=0.01, rely=0.01, relheight=0.08, relwidth=0.1)
ent_id = Entry(frameMenu)
ent_id.place(relx=0.01, rely=0.1, relheight=0.08, relwidth=0.1)

lb_disciplina = Label(frameMenu,text="DISCIPLINA",bg="#fffaf0",font=('Helvetica', 11, 'bold'))
lb_disciplina.place(relx=0.01, rely=0.2, relheight=0.08, relwidth=0.12)
ent_disciplina = Entry(frameMenu)
ent_disciplina.place(relx=0.01, rely=0.29, relheight=0.08, relwidth=0.1)

lb_av1 = Label(frameMenu,text="AV1",bg="#fffaf0",font=('Helvetica', 11, 'bold'))
lb_av1.place(relx=0.01, rely=0.39, relheight=0.08, relwidth=0.1)
ent_av1 = Entry(frameMenu)
ent_av1.place(relx=0.01, rely=0.47, relheight=0.08, relwidth=0.1)

lb_av2 = Label(frameMenu,text="AV2",bg="#fffaf0",font=('Helvetica', 11, 'bold'))
lb_av2.place(relx=0.01, rely=0.57, relheight=0.08, relwidth=0.1)
ent_av2 = Entry(frameMenu)
ent_av2.place(relx=0.01, rely=0.65, relheight=0.08, relwidth=0.1)

lb_av3 = Label(frameMenu,text="AV3",bg="#fffaf0",font=('Helvetica', 11, 'bold'))
lb_av3.place(relx=0.01, rely=0.75, relheight=0.08, relwidth=0.1)
ent_av3 = Entry(frameMenu)
ent_av3.place(relx=0.01, rely=0.83, relheight=0.08, relwidth=0.1)

lb_avd = Label(frameMenu,text="AVD",bg="#fffaf0",font=('Helvetica', 11, 'bold'))
lb_avd.place(relx=0.16, rely=0.01, relheight=0.08, relwidth=0.1)
ent_avd = Entry(frameMenu)
ent_avd.place(relx=0.16, rely=0.1, relheight=0.08, relwidth=0.1)

lb_avds = Label(frameMenu,text="AVDS",bg="#fffaf0",font=('Helvetica', 11, 'bold'))
lb_avds.place(relx=0.16, rely=0.2, relheight=0.08, relwidth=0.1)
ent_avds = Entry(frameMenu)
ent_avds.place(relx=0.16, rely=0.29, relheight=0.08, relwidth=0.1)

#FRAMETREE
frameTree = Frame(window, bg="#fffaf0")
frameTree.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.48)

list_record = ttk.Treeview(frameTree,height=3,columns=("ID", "Disciplina", "AV1", "AV2", "AV3","AVD", "AVDS", "MEDIA", "STATUS"))

list_record.heading("ID", text="ID", anchor="center")
list_record.heading("Disciplina", text="Disciplina", anchor="center")
list_record.heading("AV1", text="AV1", anchor="center")
list_record.heading("AV2", text="AV2", anchor="center")
list_record.heading("AV3", text="AV3", anchor="center")
list_record.heading("AVD", text="AVD", anchor="center")
list_record.heading("AVDS", text="AVDS", anchor="center")
list_record.heading("MEDIA", text="MEDIA", anchor="center")
list_record.heading("STATUS", text="STATUS", anchor="center")

list_record.column('#0', stretch=NO, minwidth=0, width=1)
list_record.column('#1', stretch=NO, minwidth=0, width=90)
list_record.column('#2', stretch=NO, minwidth=0, width=90)
list_record.column('#3', stretch=NO, minwidth=0, width=90)
list_record.column('#4', stretch=NO, minwidth=0, width=90)
list_record.column('#5', stretch=NO, minwidth=0, width=90)
list_record.column('#6', stretch=NO, minwidth=0, width=90)
list_record.column('#7', stretch=NO, minwidth=0, width=90)
list_record.column('#8', stretch=NO, minwidth=0, width=90)
list_record.column('#9', stretch=NO, minwidth=0, width=107)

list_record.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.9)

scrolllist = Scrollbar(frameTree, orient='vertical')
list_record.configure(yscroll=scrolllist.set)
scrolllist.place(relx=0.98, rely=0.01, relwidth=0.02, relheight=1)
list_record.bind("<Double-1>", onDuploClick)

attention = Label(frameTree,
                  text="CLIQUE DUAS VEZES NO ITEM PARA SELECIONA-LO",
                  bg="#fffaf0")
attention.place(relx=0.024, rely=0.93, relwidth=0.95, relheight=0.055)

create_db()
onSelect()
window.mainloop()

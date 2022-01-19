import sqlite3

conn = sqlite3.connect("compras.db")

cursor = conn.cursor()

def criar_tabela():
    conn.execute("""create table if not exists compras (
        id_nºitem integer primary key autoincrement,
        nome_item text, 
        quant_item int,
        valor_item float
    )""")
def add_item(nome_item,quant_item,valor_item):
    try:
        conn.execute('insert into compras (nome_item,quant_item,valor_item) values (?, ?, ?)', (nome_item,quant_item,valor_item))
        conn.commit()
    except sqlite3.Error as error:
        print('ERRO: Falha ao inserir item da compra.', error)

def exibir_compra():
    try:
        return conn.execute('select id_nºitem, nome_item,quant_item,valor_item from compras')
    except sqlite3.Error as error:
        print('ERRO: Falha ao inserir aluno', error)

def alterar_item_compra(id_nºitem,nome_item,quant_item,valor_item):
    try:
        update_query = 'update compras set nome_item =?,quant_item =?,valor_item =? where id_nºitem =?'
        dados_alterar = (nome_item,quant_item,valor_item,id_nºitem)
        cursor.execute(update_query, dados_alterar)
        conn.commit()
    except sqlite3.Error as error:
        print('ERRO: Falha ao alterar compra', error)

def excluir_item_compra(id_nºitem):
    try:
        delete_query = 'delete from compras where id_nºitem = ?'
        dados_item = (id_nºitem, )
        cursor.execute(delete_query, dados_item)
        conn.commit()
    except sqlite3.Error as error:
        print('ERRO: Falha ao alterar compras')
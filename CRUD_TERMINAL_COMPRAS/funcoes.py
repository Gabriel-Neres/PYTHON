import banco_de_dados as banco_de_dados

def criar_nova_compra():
    try:
        nome_item = str(input("Digite o nome do item: "))
        quant_item = int(input('Digite a quantidade: '))
        valor_item = float(input('Digite o valor da compra: '))
    except Exception as e:
        print("ERRO: Ao criar compra: {}".format(e))
    else:
        banco_de_dados.add_item(nome_item, quant_item, valor_item)

def exibindo_compras():
    print("{:>2} {:<28}  {:>2} {:>10} ".format("Nº","Item","Quantidade", "Preço"))
    for dado in banco_de_dados.exibir_compra():
        exibir = "[{:>2}] {:<28}  {:>2}  {:>10} {:>2} ".format(dado[0],dado[1],dado[2], "R$", dado[3])
        print(exibir)
    
def alterando_compra():
    exibindo_compras()
    try:   
        id_nºitem = int(input("Qual compra vc gostaria de alterar? Digite o codigo: "))
    except Exception as e:
        print("ERRO: Ao alterar compra: {}".format(e))
    else:
        novo_item = str(input('Digite novo item: '))
        nova_quant = int(input('Digite quantidade de itens: '))
        novo_valor = float(input('Digite o valor do item: '))
        banco_de_dados.alterar_item_compra(id_nºitem, novo_item, nova_quant, novo_valor)

def excluindo_item():
    exibindo_compras()
    try:
        id_nºitem = int(input("Qual item vc gostaria de excluir. Digite o codigo do item: "))
    except Exception as e:
        print("ERRO: Ao excluir compra: {}".format(e))
    else:
        banco_de_dados.excluir_item_compra(id_nºitem)
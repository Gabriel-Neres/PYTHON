import banco_de_dados as banco_de_dados
import funcoes as funcoes
import datetime

data_sistema = datetime.date.today()
data = data_sistema.strftime('%d/%m/%Y')

def main():
    nomeuso = str(input("Digite seu nome: "))
    while True:
        try:
            print("Menu Principal - Seja bem vindo ao Aplicativo de compras de Mercado\n")
            print("1 - Cadastrar compra \n2 - Exibir itens\n3 - Alterar itens\n4 - Excluir itens\n5 - sair \n\n")
            escolha = int(input("Escolha sua opção: "))
        except ValueError:
                print("Opção não reconhecida.")
        else:
                if escolha == 1:
                    funcoes.criar_nova_compra()
                elif escolha == 2:
                    funcoes.exibindo_compras()
                elif escolha == 3:
                    funcoes.alterando_compra()
                elif escolha == 4:
                    funcoes.excluindo_item()
                elif escolha == 5:
                    break
                else:
                    print('Opção invalida!')
    cond = True
    while cond:
        resposta_final =int(input("Você considera o seu acesso ao aplicativo finalizado?\n1 - Sim\n2 - Não\n"))
        if (resposta_final == 1):
                final = "Aplicativo finalizado com êxito por "
                cond = False
        elif (resposta_final == 2):
                final = "Aplicativo finalizado sem êxito por "
                cond = False
        else:
            print("Resposta inválida")
    
    
    print("----- Relatório -----")
    print("Nome do usuário: ",nomeuso)
    print(final + nomeuso)
    print(data)
        

if __name__ == '__main__':
    banco_de_dados.criar_tabela()

    main()
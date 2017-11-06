import associativa as assoc
import direta as dire
import sys

def menu_principal(arquivo):
    print("#" * 50)
    print("Teste de gestao de memoria ")
    print("Selecione a opcao desejada:")
    print("0) Encerrar o programa.")
    print("1) Memoria Direta.")
    print("2) Memoria Associativa.")
    opcao = -1
    while opcao < 0 or opcao > 2:
        opcao = int(input("Opcao: "))
        if (opcao == 1):
            print("")
            dire.memoria_direta(arquivo)
        elif (opcao == 2):
            print("")
            assoc.memoria_associativa(arquivo)
        else:
            sys.exit("Programa encerrado.")



#Inicio do programa.

if len(sys.argv) != 2:
    print("")
    print("Informe somente o arquivo de texto 'acessos.txt' como parametro.")
    print("")

menu_principal(sys.argv[1])
import associativa as assoc
import direta as dire
import sys

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
        dire.direta.py
    elif (opcao == 2):
        assoc.associativa.py
    else:
        sys.exit("Programa encerrado.")

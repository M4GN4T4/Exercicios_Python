v1 = int(input("Digite o primeiro valor:"))
v2 = int(input("Digite o segundo valor:"))
print("""Escolha uma das opções abaixo:
====================
Somar[1]           |
Multiplicar[2]     |
Maior[3]           |
Novos Números[4]   |
Sair do Programa[5]|
====================""")
n = 0
while n != 5:
    n = int(input("[OPÇÃO]:"))
    if n == 1:
        print(f"A soma entre {v1} é {v2} e igual a:{v1 + v2}")
    elif n == 2:
        print(f"A Multiplicação entre {v1} é {v2} e igual a:{v1 * v2} ")
    elif n == 3:
        if v1 < v2:
            maior = v2
            print(f"O Maior valor é {maior}")
        elif v2 < v1:
            maior = v1
            print(f"O Maior valor é {maior}")
    elif n == 4:
        v1 = int(input("Digite um novo primeiro valor:"))
        v2 = int(input("Digite um novo segundo valor:"))
    elif n == 5:
        print("[Programa Encerrado]")
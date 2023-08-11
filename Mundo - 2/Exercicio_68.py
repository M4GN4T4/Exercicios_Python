import random
c = 0
Menu = "Menu"
Resultado = "Resultado"
while True:
    print(f"{Menu:=^32}")
    num = int(input("Digite um número entre[1 e 10]:"))
    opcao = str(input("Escolha entre (P/I):")).upper().strip()[0]
    computador = random.randint(0,10)
    print(f"{Menu:=^32}")
    print(f"{Resultado:=^35}")
    print(f"O Computador escolheu {computador}")
    if opcao == "P":
        s = num + computador
        if s % 2 == 0:
            print(f"No total deu {s} ")
            print("Você venceu")
            print(f"{Resultado:=^35}")
            c += 1
        else:
            print(f"No total deu {s} ")
            print("Voce Perdeu")
            print(f"{Resultado:=^35}")
            break
    elif opcao == "I":
        s = num + computador
        if s % 2 == 1:
            print(f"No total deu {s}")
            print("Você venceu")
            print(f"{Resultado:=^35}")
            c += 1
        else:
            print(f"No total deu {s}")
            print("Voce Perdeu")
            print(f"{Resultado:=^35}")
            break
print(f"Você venceu {c} vezes antes de perde!")
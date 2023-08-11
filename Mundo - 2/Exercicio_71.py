s = int(input("Digite o valor do saque R$:"))
t = s
c = 50
tc = 0
while True:
    #Decrementador enquanto "t" não chegar a zero o comando não termina
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            print(f"Total de {tc} cédulas de R${c}")
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        #tc iguala a zero para quando passar no print dar a nota exata da quantidade de notas ! 
        #  que passa no loopin de cima
        tc = 0
        if t == 0:
            break
print("Programa Encerrado")
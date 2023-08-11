print("Digite um número negativo para parar")
while True:
    n = int(input("Deseja ver a tabuada de qual número:"))
    if n < 0:
        break
    for x in range(1,11,1):
        print(f"{x} X {n} = {n * x}")
print("Acabou")
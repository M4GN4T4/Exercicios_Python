num1 = 0
for n in range(0,6):
    num = int(input("Digite o valor de um número:"))
    if num % 2 == 0:
        num1 += num
        print(f"{num1} + {num} = {num1 + num}")
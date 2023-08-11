def leiaint(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print(f"\033[0;31mErro! Digite um número inteiro valido.\033[m")
            

n = leiaint("Digite um número:")
print(f"Você acabou de digitar o número {n}")
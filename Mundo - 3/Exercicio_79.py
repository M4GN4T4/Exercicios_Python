Num = []
p = 0
while True:
    n = int(input("Digite um valor:"))
    if n not in Num:
        Num.append(n)
    else:
        print("Valor duplicado não vou adicionar...")
    opcao = str(input("Quer continuar ? [S/N]")).upper()
    if opcao == "N":
        break 
Num.sort() 
print(Num)
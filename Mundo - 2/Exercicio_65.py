c = total = 0
parar = "S"
#parar = " "
#menor = 100
while parar in "Ss":
    num = int(input("Digite números inteiros:"))
    c += 1
    total += num
    if c == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
#    if menor > num:
#        menor = num
#    if maior < num:
#        maior = num
    parar = str(input("Quer continuar a digitar valores ? (S/N):")).upper().strip()[0]
print(f"A media é {total/c}\nO Menor número é {menor}\nO Maior número é {maior}")
print("Fim")
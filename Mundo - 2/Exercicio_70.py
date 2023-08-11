total = c = 0
while True:
    nome = str(input("Digite o nome do produto:"))
    pp = float(input("Digite o preço do produto:"))
    total += pp
    menor = pp
    if pp > 1000:
        c += 1
    if c == 1 or pp < menor:
        mp = nome
        menor = pp
    opcao = " "
    while opcao not in "SN":
        opcao = str(input("Quer continuar[S/N]:")).upper().strip()[0]
    if opcao == "N":
        break
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {c} Produtos custando mais de R$1000")
print(f"O produto mais barato foi {mp} que custa R${menor:.2f}")
p = float(input("Digite o valor do produto:"))
print(25 * "=","\n[1] A vista em dinheiro||\n[2] No cartão/Parcelado||\n",24 * "=")
o = int(input("Digite a [OPÇÃO]:"))
if o == 1:
    print(f"Compra a vista tem 10% de Desconto ou seu desconto foi {p * 0.10} totalizando:{p - (p * 0.10)}")
elif o == 2:
    print(25 * "=", "\n[1] A vista            ||\n[2] Parcelado          ||\n", 24 * "=")
    o2 = int(input("Digite a [OPÇÃO]:"))
    if o2 == 1:
        print(f"Compra a vista no cartão tem 5% de Desconto ou seu desconto foi {p * 0.05} totalizando:{p - (p * 0.05)}")
    elif o2 == 2:
        pa = int(input("Quantas Parcelas deseja pagar:"))
        if pa <= 2:
            print(f"Você ira pagar {pa} parcelas de:{p / pa}")
        elif pa > 2:
            print(f"Você ira pagar {pa} parcelas com 20% a mais de juro totalizando:{(p / pa) + p * 0.20:.2f} por parcela")
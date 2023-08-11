valor = float(input("Digite o valor da casa:"))
salario = float(input("Digite o salário do comprador:"))
anos = int(input("Em quantos anos ele ira pagar:"))

if salario * 0.30 < valor / (anos * 12):
    print(f"O valor \33[;44m{valor / (anos * 12)}\33[m está acima de 30% que corresponde a \33[;44m{salario * 0.30}\33[mdo seu salário pedido negado")
else:
    print(f"Pedido Aceito\n O valor da parcela ficou estimado em \33[;44m{valor / (anos * 12):.2f}\33[m")

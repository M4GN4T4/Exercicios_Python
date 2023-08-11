def metade(n, form=False):
    r = n / 2
    return r if form is False else moeda(r)

   
def dobro(n = 0, form=False):
    r = n * 2
    return r if form is False else moeda(r)


def aumentar(n = 0, por = 0, form=False):
    r = n + (n * (por / 100))
    return r if form is False else moeda(r)


def diminuir(n = 0, por = 0, form=False):
    r = n - (n * (por / 100))
    return r if form is False else moeda(r)


def moeda(preço = 0, moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('.', ',')
 

def resumo(n, porp=0, porn=0):
    tit = "RESUMO DO VALOR"
    print("-" * 35)
    print("RESUMO DO VALOR".center(35))
    print("-" * 35)
    print(f"Preço analisado: \t{moeda(n)}")
    print(f"Dobro do preço: \t{dobro(n, True)}")
    print(f"Metade do preço: \t{metade(n, True)}")
    print(f"{porp}% de aumento: \t{aumentar(n, porp, True)}")
    print(f"{porn}% de redução: \t{diminuir(n, porn, True)}")
    print("-" * 35)

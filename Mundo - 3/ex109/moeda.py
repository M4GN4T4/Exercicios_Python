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
 
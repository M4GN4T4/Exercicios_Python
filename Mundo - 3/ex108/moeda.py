def metade(n):
    r = n / 2
    return r


def dobro(n = 0):
    r = n * 2
    return r


def aumentar(n = 0, por = 0):
    r = n + (n * (por / 100))
    return r


def diminuir(n = 0, por = 0):
    r = n - (n * (por / 100))
    return r


def moeda(preço = 0, moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('.', ',')


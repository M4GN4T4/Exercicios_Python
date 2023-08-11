def fatorial(n, Show=False):
    """-> Calcula o fatorial de um número.
    :parametro [n]: número a ser calculado
    :parametro [show]: Opcional mostar ou não a conta
    :return: O Valor do Fatorial de um número n.
    """

    m = 1
    while n > 0: 
        m *= n

        if Show:
            print(n, end="",)
            if n > 1:
                print(end=" X ")
            else:
                print(end=" = ")

        n = n - 1

    return print(m)
fatorial(5)

help(fatorial)
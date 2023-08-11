def leiaDinheiro(msg):
    while True:
        num = str(input(msg)).replace(',', '.')
        if num.isalpha():
            print(f"\033[0;31mErro {num} é um preço inválido.\033[m")
        else:
            return float(num)
def leiaDinheiro(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num.replace(',', '.'))
            return int(num)
        else:
            print(f"\033[0;31mErro! {num} é um preço invalido.\033[m")
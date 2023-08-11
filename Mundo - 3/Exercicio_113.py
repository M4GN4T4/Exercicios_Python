def leiaint(msg):
    while True:
        try:
            num = int(input(msg))              
        except (ValueError, TypeError):
            print(f"\033[0;31mErro: por favor, Digite um número inteiro valido.\033[m")
        except KeyboardInterrupt:
            print(f"\n\033[0;31mErro: O usuário prefiriu não informar os dados.\033[m")
            return 0
        else:
            return num


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))              
        except (ValueError, TypeError):
            print(f"\033[0;31mErro: por favor, Digite um número real valido.\033[m")
        except KeyboardInterrupt:
            print(f"\n\033[0;31mErro: O usuário prefiriu não informar os dados.\033[m")
            return 0
        else:
            return num


n1 = leiaint("Digite um número inteiro:")
n2 = leiafloat("Digite um número Real:")
print(f"O valor inteiro digitado foi {n1} e o real foi {n2}")

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


def linha(tam = 42):
    return "-" * 42


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[36m{item}\033[m")
        c += 1
    linha
    opc = leiaint("\033[32mSua Opção:\033[m")
    return opc
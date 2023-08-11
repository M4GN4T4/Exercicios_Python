def titulo(tit):
    print("\033[0;30;42m~\033[m" * (len(tit) + 4))
    print(f"\033[0;30;42m  {tit}  \033[m")
    print("\033[0;30;42m~\033[m" * (len(tit) + 4))


def acesso(tit):
    print("\033[7;36;40m~\033[m" * (len(tit) + 4))
    print(f"\033[7;36;40m  {tit}  \033[m")
    print("\033[7;36;40m~\033[m" * (len(tit) + 4))

#def ajuda(com):
    #help(com)

while True:
    titulo("Sistema de Ajuda PyHELP")
    perg = str(input("Função ou Biblioteca >")).strip()
    acesso(f"Acessando o manual do comando {perg}")
    if perg == 'FIM':
        break
    else:
        help(perg)
titulo("Ate Logo")
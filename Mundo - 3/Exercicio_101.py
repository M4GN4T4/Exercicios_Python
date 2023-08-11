def voto (ano):
    from datetime import date
    
    i = date.today().year - ano
    if i  < 16:
        return f"você tem {i}, [VOTO NEGADO]"
    elif i < 18 or i > 65:
        return f"você tem {i}, [VOTO OPCIONAL]"
    else:
        return f"você tem {i}, [VOTO OBRIGATÓRIO]"
    

n =  int(input("Digite em que ano você nasceu:"))
print(voto(n))
C_d_P = []
n = str(input("Digite a expressão:")).strip(' ')
for simb in n:
    if simb == "(":
        C_d_P.append("(")
    elif simb == ")":
        if len(C_d_P) > 0:
            C_d_P.pop()
        else:
            C_d_P.append(")")
            break
if len(C_d_P) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")
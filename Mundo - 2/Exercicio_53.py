p = str(input("Digite um palavra ou frase:")).strip(" ")
a = p.replace(" ", "")

if a == a[::-1]:
    print("E um palindromo")
else:
    print("Não e um Palindromo")
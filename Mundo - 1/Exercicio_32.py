n = int(input("Digite um ano aleatorio:"))
a = 16 % 400
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Esse ano e Bissexto")
else:
    print("Esse ano não e Bissexto")

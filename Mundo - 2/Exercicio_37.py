n = int(input("Digite o valor:"))
print("Escolha um das opções abaixo\nConverte para Binário[1]\nConverte para Octal[2]\nConverte para Hexadecimal[3]")
escolha = int(input(">>>>:"))
if escolha == 1:
    b = bin(n)
    print(f"Binário:{b.lstrip('-0b')}")
elif escolha == 2:
    o = oct(n)
    print(f"Octal:{o}")
elif escolha == 3:
    h = hex(n)
    print(f"Hexadecimal:{h}")
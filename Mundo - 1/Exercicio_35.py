l1 = int(input("Digite um número para o segmento [1]:"))
l2 = int(input("Digite um número para o segmento [2]:"))
l3 = int(input("Digite um número para o segmento [3]:"))

if l1 + l2 >= l3 and l2 + l3 >= l1 and l2 + l3 >= l3:
    print("E possivel formar um triangulo")
else:
    print("Não e possivel formar um triangulo com esses valores")
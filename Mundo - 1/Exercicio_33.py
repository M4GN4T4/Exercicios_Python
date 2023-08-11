n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))
n3 = int(input("Digite um número:"))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Lista = [n1, n2, n3]
#print(f"O Maior valor é {max(Lista)}")
#print(f"O menor valor é {min(Lista)}")

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f"O Menor valor digitado foi:{menor}")
print(f"O Maior valor digitado foi:{maior}")
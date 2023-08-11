n = int(input("Digite um número entre 0 é 9999:"))
u =   n // 1 % 10
d =   n // 10 % 10
c =   n // 100 % 10
m =   n // 1000 % 10

print(f"O Número escolhido tem {u} unidades")
print(f"O Número escolhido tem {d} dezenas")
print(f"O Número escolhido tem {c} centenas")
print(f"O Número escolhido tem {m} milhas")
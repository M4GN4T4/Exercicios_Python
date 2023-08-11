p1 = int(input("Digite o primeiro termo:"))
r = int(input("Digite a razão:"))
decimo = p1 + (11-1) * r
for n in range(p1, decimo, r):
    print(n, end=" --> ")
print("Fim")
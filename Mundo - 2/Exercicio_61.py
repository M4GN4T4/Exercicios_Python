p1 = int(input("Digite o primeiro termo:"))
pa = int(input("Digite a razão:"))
r = p1
decimo = p1 + (10 * pa)
while r < decimo:
    r += pa
    print(r, end=" --> ") 
print("Fim")

#p1 = int(input("Digite o primeiro termo:"))
#r = int(input("Digite a razão:"))
#decimo = p1 + (11-1) * r
#for n in range(p1, decimo, r):
#    print(n, end=" --> ")
#print("Fim")
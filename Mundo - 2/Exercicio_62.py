p1 = int(input("Digite o primeiro termo:"))
r = int(input("Digite a razão:"))
pa = p1
#decimo = p1 + (10 * pa)
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        pa += r
        cont += 1
        print(pa, end=" --> ") 
    print("Pausa")
    mais = int(input("Quantos termos a mais você quer mostrar:"))
print("Fim")
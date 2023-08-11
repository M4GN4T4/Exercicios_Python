import time
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("-=" * 20)
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=' ', flush=True)
            cont += p
        print("Fim")
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=' ', flush=True)
            time.sleep(0.5)
            cont -= p
        print("Fim")


#if passo == 0:
#    passo = -1
#print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
#for _ in range(inicio, fim, passo):
#    time.sleep(0.5)
#    print(_, end=' ', flush=True)
#print("Fim")

contador(1, 10, 1)
contador(10, 0, -2)
print(20 * "-=")
print("Agora e sua vez personalizar a contagem!")

ini = int(input("Início:"))
fim = int(input("Fim:"))
pas = int(input("Passo:"))
contador(ini, fim, pas)
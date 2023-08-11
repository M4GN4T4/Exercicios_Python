qtd = int(input("Digite Quantos termos deseja ver da Sequência Fibonacci:"))
c = 3
t1 = 0
t2 = 1
print(f" {t1} --> {t2}", end=' --> ')
while c <= qtd:
    c += 1
    t3 = t1 + t2 
    print(t3, end=' --> ')
    t1 = t2
    t2 = t3
print('Fim')
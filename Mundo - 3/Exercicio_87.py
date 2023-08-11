Matriz = [[], [], []]
tp = maior = t3c = 0
for l in range(0, 3):
    for c in range(0, 3):
        Matriz[l].append(int(input(f"Digite um valor para [{l},{c}]:")))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{Matriz[l][c]:^5}", end="]")
        if Matriz[l][c] % 2 == 0:
            tp += Matriz[l][c]
    print()

for l in range(0, 3):
    t3c += Matriz[l][2]
for c in range(0, 3):
    # if c == 0 or Matriz[1][c] > maior:
    if c == 0:
        maior = Matriz[1][c]
    elif Matriz[1][c] > maior:
        maior = Matriz[1][c]

print(f"A) a soma de todos os números pares digitados:{tp}")
print(f"B) a soma dos valores da terceira coluna:{t3c}")
print(f"C) o maior valor da segunda linha:{maior}")
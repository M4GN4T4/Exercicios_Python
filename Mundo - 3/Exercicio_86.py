Matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        Matriz[l].append(int(input(f"Digite um valor para [{l},{c}]:")))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{Matriz[l][c]:^5}", end="]")
    print()
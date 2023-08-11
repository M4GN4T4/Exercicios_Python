T = [[], []]

# Registrando_Números.
for _ in range(0, 7):
    n = int(input(f"Digite {_+1} número:"))
    # Separando_Pares_é_Impares
    if n % 2 == 0:
        T[0].append(n)
    elif n % 2 == 1:
        T[1].append(n)

# T[0].sort()
# T[1].sort()
print(f"Os valores pares digitados foram:{sorted(T[0])}")
print(f"Os valores Impares digitados foram:{sorted(T[1])}")

"""
# Separando_Pares_é_Impares
for n in T:
    if n % 2 == 0:
        p.append(n)
    elif n % 2 == 1:
        i.append(n)
# Juntando_Listas
C = sorted(p) + sorted(i)
print(C)
"""
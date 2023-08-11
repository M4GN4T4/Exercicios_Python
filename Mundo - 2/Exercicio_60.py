mul = 1
n = int(input("Digite um número e veja seu fatorial:"))
print(f"O fatorial de {n}:", end=" ")
while n > 0:
    print(n, end="")
    print(" x " if n > 1 else " = ", end='')
    mul *= n
    n -= 1
print(f"{mul}")

print(50 * "+")

mul = 1
n = int(input("Digite um número e veja seu fatorial:"))
print(f"O fatorial de {n}:", end=" ")
for num in range(n, 0, -1):
    mul *= num
    print(num, end="")
    print(" x " if num != 1 else " = ", end='')
print(f"{mul}")
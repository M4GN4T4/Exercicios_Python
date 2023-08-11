maior = 0
menor = 0
for x in range(0, 5):
    peso = float(input(f"Digite o Peso da pessoas [{x+1}]:"))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
print(f"O Maior peso é:{maior}")
print(f"O menor peso e:{menor}")

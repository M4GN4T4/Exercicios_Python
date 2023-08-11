soma = 0
velho = 0
contador = 0
nome_velho = ""
for x in range(1, 5):
    nome = str(input(f"Digite o nome da pessoa [{x}]:"))
    idade = int(input(f"Digite a idade da pessoa [{x}]:"))
    sexo = str(input(f"Digite seu sexo [Masculino/Feminino] da pessoa [{x}]:")).lower().capitalize()
    soma += idade
    if sexo == "Feminino":
        if idade < 20:
            contador += 1
    if sexo == "Masculino":
        if velho < idade:
            velho = idade
            nome_velho = nome
print(f"Homem mais velho é {nome_velho} ele tem [{velho}] anos")
print(f" A media de idades é:{soma / 4}")
print(f" Existem {contador} mulheres abaixo dos 20 anos!")
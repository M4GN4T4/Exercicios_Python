idade = str(input("Digite sua data de Nascimento:"))
data = idade.split("/")
data1 = int(data[2])
ano = 2023 - data1

if ano  <= 9:
    print(f"Você tem {ano} anos faz parte da categoria:MIRIM")
elif ano <= 14:
    print(f"Você tem {ano} anos faz parte da categoria:INFANTIL")
elif ano <= 19:
    print(f"Você tem {ano} anos faz parte da categoria:JUNIOR")
elif ano <= 20:
    print(f"Você tem {ano} anos faz parte da categoria:SÊNIOR")
elif ano > 20:
    print(f"Você tem {ano} anos faz parte da categoria:MASTER")
n = str(input("Digite a sua data de nascimento:"))
data = n.split("/")
data1 = int(data[2])
ano = 2023 - data1

if ano <= 17:
    print("Ainda vai-se alistar ao Serviço Militar")
    print(f"Ainda falta {18 - ano} ano para se Alistar")
elif ano == 18:
    print("Hora de se Alistar")
elif ano > 18:
    print("Passou do tempo de Alistamento")
    print(f"Ja passou {ano - 18} ano do prazo para se Alistar")


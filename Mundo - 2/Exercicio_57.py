s = str(input("Informe seu sexo [M/F]:")).strip().upper()[0]
while s not in "MF":
    s = str(input("Dados Inválidos, Por favor, informe seu sexo:")).strip().upper()[0]
print(f"Sexo {s} registrado com sucesso")
#while s != "M" and s != "F":
 #   s = str(input("Digite o O Sexo [M/F]:")).upper()
  #  s = s
   # if s not in "MF":
    #    print("Digite Novamente")
#print("Sexo Cadrastado com Sucesso")
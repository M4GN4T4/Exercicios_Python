n= input("Digite qualquer coisa:")

print("Só tem espaços ?", n.isspace())
print("É um número ?", n.isnumeric())
print("É alfabetico ?", n.isalpha())
print("É alfanúmerico ?", n.isalnum())
print("Está em maiúscula ?", n.isupper())
print("Está em minúscula ?", n.islower())
print("Está captalizada ?", n.istitle())
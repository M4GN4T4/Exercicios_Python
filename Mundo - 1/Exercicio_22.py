nome = str(input("Digite o seu nome completo:")).strip("+-.*-0987654321!@#$%¨&*()<> :")
Primeiro_nome = nome.split()
print(f"Seu nome completo Maiúsculo:{nome.upper()}")
print(f"Seu nome completo Minúsculo:{nome.lower()}")
print(f"Seu nome sem Espaços:{len(nome)-nome.count(' ')}")
#print(f"Seu primeiro nome é {Primeiro_nome[0]} tem {len(Primeiro_nome[0])} letras")
print(f"Seu primeiro nome tem {nome.find(' ')} letras")


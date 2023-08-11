frase = str(input("Digite uma Frase:")).upper()
q_d_a = frase.count("A") 
pa = frase.find("A")+1
ua = frase.rfind("A")+1

print(f"O (a) Apareceu:{q_d_a}")
print(f"O primeiro (a) Apareceu na posição:{pa}")
print(f"O ultimo (a) Apareceu na posição:{ua}")
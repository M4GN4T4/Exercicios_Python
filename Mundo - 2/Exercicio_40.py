n1 = float(input("Digite a primeria nota do aluno:"))
n2 = float(input("Digite a segunda nota do aluno:"))

if 0 <=(n1 + n2) / 2 <= 5:
    print("Você está Reprovado")
elif 5 <= (n1 + n2) / 2  <= 6.9:
    print("Você está de Recuperação")
elif (n1 + n2) / 2 >= 7:
    print("Você está Aprovado")
print(f"Sua media foi {(n1 + n2) / 2}")

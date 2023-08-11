Aluno = dict()
Aluno["nome"] = str(input("Nome:"))
Aluno["media"] = float(input(f"A Média de {Aluno['nome']}:"))
print(20 * "=")
print(f"Nome é igual {Aluno['nome']}")
print(f"Média é igual a {Aluno['media']}")
if Aluno['media'] >= 7:
    Aluno['situacao'] = "Aprovado"
elif 5 <= Aluno['media'] >= 7:
    Aluno['situacao'] = "Recuperação"
else:
    Aluno['situacao'] = "Reprovado"
for k, i in Aluno.items():
    print(f">>>>{k} é igual a {i}")
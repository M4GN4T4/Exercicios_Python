Cadastro = dict()
# Inserindo_dados
Cadastro['Nome'] = str(input("Nome:"))
Ano = int(input("Ano de Nascimento:"))
Cadastro['Idade'] = 2023 - Ano
Cadastro['CTPS'] = int(input("Carteira de trabalho:"))
print(25 * "=")
if Cadastro['CTPS'] != 0:
    Cadastro['Contratação'] = int(input("Ano de Contratação:"))
    Cadastro['Salário'] = float(input("Salário:"))
    print(25 * "=")
    Cadastro['Aposentadoria'] = ((Cadastro['Idade'] + Cadastro['Contratação'] + 35) - 2023)
for k, v in Cadastro.items():
    print(f"  - {k} Tem o valor:{v}")
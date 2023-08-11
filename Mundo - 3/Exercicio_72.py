num = ("Zero","Um","Dois","Três","Quatro","Cinco",
       "Seis","Sete","Oito","Nove","Dez",
       "Onze","Doze","Treze","Quatorze","Quinze",
       "Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")
while True:
       while True:
              n = int(input("Digite um número entre 0 e 20:"))
              if 0 <= n <= 20:
                     break
              print("Tente Novamente " , end="")
       print(f"Você digitou o número {num[n]}")
       opcao = str(input("Quer continuar [S/N]")).upper().strip()[0]
       if opcao == "N":
              break
print("Programa Encerrado")

#while True:
#       while True:
#              n = int(input("Digite um número entre 0 e 20:"))
#              if 0 <= n <= 20:
#                     break
#       for x,p in enumerate(num):
#             if x == n:
#                    print(f"Você digitou o número {p}")
#       opcao = str(input("Quer continuar [S/N]")).upper().strip()[0]
#       if opcao == "N":
#              break
Tabela = ("Lápis", 1.75,
          "Borracha", 2.00, 
          "Caderno", 15.90, 
          "Estojo", 25.00, 
          "Transferidor", 4.20, 
          "Compasso", 9.99, 
          "Mochila", 120.32 , 
          "Canetas", 22.30, 
          "Livro", 34.90)
Menu = "Menu"
print(40 * "=")
print(f"{'Menu':-^40}")
print(40 * "=")
for p, n in enumerate(Tabela):
    if p % 2 == 0:
        print(f"{n:.<30}", end="|R$ ")
    else:
#    if p % 2 == 1:
        print(n)
print(40 * "=")
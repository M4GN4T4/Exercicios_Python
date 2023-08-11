Lista_Palavras = ("Aprender", 
                  "Programar", 
                  "Linguagem", 
                  "Python", 
                  "Curso", 
                  "Gratis", 
                  "Estudar", 
                  "Praticar", 
                  "Trabalhar", 
                  "Mercado", 
                  "Programador", 
                  "Futuro")

for p in (Lista_Palavras):
    print(f"\nNa palavra {p} temos:", end=" ")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
       


        
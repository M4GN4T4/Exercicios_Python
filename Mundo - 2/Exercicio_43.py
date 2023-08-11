peso = float(input("Digite o seu peso:"))
altura = float(input("Digite a sua Altura:"))
IMC = peso / (altura * altura)

if IMC <= 18.5:
    print(f"IMC:{IMC:.1f} Você está abaixo do peso")
elif IMC <= 25:
    print(f"IMC:{IMC:.1f} Peso Ideal")
elif IMC <= 30:
    print(f"IMC:{IMC:.1f} Sobrepeso")
elif IMC <= 40:
    print(f"IMC:{IMC:.1f} 0besidade")
elif IMC > 40:
    print(f"IMC:{IMC:.1f} Obesidade Morbida")
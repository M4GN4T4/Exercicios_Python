import math
angulo = float(input("Digite o Angulo:"))
cos = math.cos(math.radians(angulo))
sen = math.sin(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f"O cosseno {cos:.2f} seno {sen:.2f} tangente {tan:.2f} do angulo {angulo}º")
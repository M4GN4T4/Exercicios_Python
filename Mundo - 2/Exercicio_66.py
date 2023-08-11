c = s = 0
print("Para parar digite [999]")
while True:
    num = int(input("Digite um número:"))
    if num == 999:   
        break 
    s += num 
    c += 1
print(f"Foram digitados {c} números a soma entre eles é {s}")
c = total = num = 0
print("Para parar digite [999]")
while num != 999:
    c += 1
    num = int(input("Digite os números que deseja somar:"))
    if num != 999:
        total += num
print(f"Foram digitados {c} números a soma total deles é:{total}")
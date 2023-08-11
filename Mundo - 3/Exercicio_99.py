import time
def maior(* num):
    print(30 * '-=')
    print("Analisando os valores Passados...")
    maior = c = 0
    for _ in num:
        c += 1
        if _ > maior:
            maior = _
        time.sleep(0.5)
        print(_, end=' ', flush=True)
    print(f"Foram informados {c} valores ao todo.")
    print(f"O Maior valor inforamdo foi {maior}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

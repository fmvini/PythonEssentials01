c0 = int(input("Digite um numero: "))
etapas = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = (c0 * 3) + 1 
    print(c0)
    etapas += 1
print(f"etapas = {etapas}")
s = int(0)
for c in range (1,7):
    esc = int(input(f'Digite o {c}º valor: '))
    if esc % 2 == 0:
        s += esc
print(f'A soma dos valores pares é igual a {s}')
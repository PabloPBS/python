s = int(0)
quant = int(0)
for c in range (1,501,2):
    if c%3==0:
        s += c
        quant = quant+1
print(f'A soma de todos os {quant} valores solicitados é igual a {s}.')

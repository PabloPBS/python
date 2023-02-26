print('-------- SOMADOR MASTER --------')
resp = int(0)
quant = int(-1)
soma = int(0)
while resp != 999:
    quant += 1
    soma += resp
    resp = int(input('Digite um número inteiro: (999 para cancelar): '))
print(f'Foram digitados [{quant}] valores, e a soma de todos eles é igual a: [{soma}].')

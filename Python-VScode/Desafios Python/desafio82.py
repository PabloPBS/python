lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? (S/N) ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Resposta inválida. Dijite S/N: ')).strip().upper()
    if resp == 'N':
        break
for c in range (0,len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(f'Lista principal: {lista}')
print(f'Lista de números pares: {pares}')
print(f'Lista de números ímpares: {impares}')

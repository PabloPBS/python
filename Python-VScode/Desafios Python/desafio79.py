lista = []
c = 0
while True:
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
    for c in lista:
        if lista.count(c) >= 2:
            print('Valor duplicado. Tente novamente.')
            lista.remove(c)
        else:
            print('Valor registrado com sucesso.')
    resp = str(input('Deseja continuar? (S/N) ')).strip().upper()
    if resp == 'N':
        break
print(lista.sort())
lista = []

while True:
    val = int(input('Digite um valor: '))

    if val in lista:
        print('Valor já adicionado. Não irei adicionar.')
    else:
        print('Valor adicionado com sucesso.')
        lista.append(val)
    
    res = str(input(('Deseja continuar? [S/N] '))).strip().upper()
    if res == 'N':
        break

print('-=-' * 20)

lista.sort()
print(f'Você digitou os valores {lista}')
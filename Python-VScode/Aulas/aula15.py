'''cont = int(0)
while True:
    print(cont, end=' > ')
    cont += 1
print('Acabou!')'''

n = s = int(0)
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')

n = c = 1
while True:
    n = int(input('Digite um valor e sua tabuada será exibida.\n(Digite um valor negativo para cancelar): '))
    if n < 0:
        break
    print('-'*20,'TABUADA', '-'*20)
    for c in range (1,11):
        print(f'{n} x {c} =', n*c)
    print('-'*40)
print('Programa TABUADA encerrado.')

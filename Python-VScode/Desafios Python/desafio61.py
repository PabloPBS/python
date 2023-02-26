c = int(0)
pri = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
print(pri, end=' > ')
while c != 10:
    prox = pri + raz
    pri = prox
    print(prox, end=' > ')
    c += 1
print('FIM!')

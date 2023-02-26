from random import randint
res = str
c = tot = 0
print('-=-'*10)
print('         PAR OU IMPAR')
print('-=-'*10)
while True:
    num = int(input('Diga um valor: '))
    esc = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    pc = randint(0,11)
    tot = num + pc
    print('--'*15)
    print(f'Você jogou {num} e o computador jogou {pc}. Total de {tot}', end=' ') 
    if tot%2==0: 
        print('DEU PAR.') 
        res = 'P'
    else: 
        print('DEU ÍMPAR')
        res = 'I'
    if esc == res:
        print('--'*15)
        print('VOCÊ VENCEU!')
        print('Vamos outra rodada...')
        c += 1
    else:
        print('--'*15)
        print(f'GAME OVER! Você venceu {c} vezes.')
        break

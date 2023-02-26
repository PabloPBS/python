from random import randint
from time import sleep
esc = int(-1)
rand = randint(0,10)
tent = int(0)
print('Sou seu computador...')
sleep(1)
print('Pensei em um número entre 0 e 10...')
sleep(1)
print('Tente sua sorte:', end=' ')
sleep(1)
while esc != rand:
    esc = int(input(''))
    if esc != rand:
        print('Errado, Tente novamente.')
        tent += 1
        if esc < rand:
            print('Minha escolha é maior...')
        else:
            print('Minha escolha é menor...')
print('Parabéns!')
print(f'Foram necessárias {tent+1} tentativas para você ganhar.')
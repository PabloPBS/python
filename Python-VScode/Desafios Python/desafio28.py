from random import randint
from time import sleep
print('Pensei em um número. Qual o seu palpite?')
esc = int(input('Tente adivinhar um número entre 0 e 5: '))
esc1 = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if esc1 == esc:
    print('\033[1;32mParabéns! Você acertou!\033[m')
else:
    print('\033[1;31mVocê errou..\033[m')
    print(f'\033[1;34mEscolha do computador: {esc1}')

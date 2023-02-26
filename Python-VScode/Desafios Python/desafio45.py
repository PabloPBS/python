from random import randint
esc = int(input('Faça sua escolha: \n 1 - Pedra \n 2 - Papel \n 3 - Tesoura \n'))
pc = randint(1,3)
if esc == 1:
    esc1 = str('Pedra')
    if pc == 1:
        print('Empate!')
    elif pc == 2:
        print('Derrota!')
    elif pc == 3:
        print('Vitória')
if esc == 2:
    esc1 = str('Papel')
    if pc == 1:
        print('Vitória!')
    elif pc == 2:
        print('Empate!')
    elif pc == 3:
        print('Derrota!')
if esc == 3:
    esc1 = str('Tesoura')
    if pc == 1:
        print('Derrota!')
    elif pc == 2:
        print('Vitória!')
    elif pc == 3:
        print('Empate!')
if pc ==1:
    pc1 = str('Pedra')
elif pc == 2:
    pc1 = str('Papel')
elif pc ==3:
    pc1 = str('Tesoura')
print(f'Sua escolha: {esc1}')
print(f'Escolha do computador: {pc1}')
esc = int(input('Digite um número inteiro e você verá o seu fatorial: '))
fat = int(1)
print(f'Calculando o fatorial de {esc}! = ', end='')
while esc != 1:
    fat = esc * fat
    print(f'{esc} x ', end = '')
    esc -= 1
print(f'1 = {fat}')

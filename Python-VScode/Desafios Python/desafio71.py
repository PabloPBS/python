'''valor = int(input('Qual o valor a ser sacado? R$'))
ced1 = ced10 = ced20 = ced50 = int(0)
ced50 = valor//50
valor = valor%50
ced20 = valor//20
valor = valor%20
ced10 = valor//10
valor = valor%10
ced1 = valor//1
valor = valor%1
print(f'Cédulas de 50: {ced50}')
print(f'Cédulas de 20: {ced20}')
print(f'Cédulas de 10: {ced10}')
print(f'Cédulas de 1:  {ced1}')
print('Tenha um bom dia.')'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totced = 0
while True:
    if total >= céd:
        total -= céd
        totced += 1
    else:
        if totced >0:
            print(f'Total de {totced} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totced=0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao bacon Cev! Tenha um bom dia!')

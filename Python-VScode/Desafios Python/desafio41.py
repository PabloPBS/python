import datetime
nasc = int(input('Digite seu ano de nascimento: '))
ano = datetime.date.today().year
idade = ano-nasc
if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade > 9 and idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL ')
elif idade > 14 and idade <= 19:
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade > 19 and idade <=20:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')
print('Sua idade é:', (idade), 'anos.')
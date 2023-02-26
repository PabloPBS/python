from datetime import date
ano = int(input('Digite o ano: (Digite 0 paa o ao atual)'))
if ano == 0:
    ano = date.today().year
    print('Ano obtido: ', ano)
if ano%4==0 and ano % 100!=0 or ano%400==0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')

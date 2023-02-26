n1 = float(input('Digite  a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média é: {m:.1f}')
if m>=7:
    print('Você está aprovado!')
else:
    if m>=5 and m<7:
        print('Você está de recuperação.')
    else:
        print('Você está reprovado.')
print('-'*10,'Programa encerrado','-'*10)

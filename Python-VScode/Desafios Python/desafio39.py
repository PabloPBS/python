import datetime
nasc = int(input('Digite seu ano de nascimento: '))
sexo = str(input('Digite seu sexo (F/M): '))
ano = datetime.date.today().year
if sexo == 'M':
    idade = ano - nasc
    if idade < 18:
        print('Você não possui idade suficiente para o alistamento militar.')
        print('Falta/am ', (18-idade), 'ano/os para seu alistamento.')
    elif idade == 18:
        print('Você deve se alistar neste ano.')
    else:
        print('Seu tempo de se alistar já passou.')
        print('Já se passaram', (idade-18), 'ano/os do seu alistamento.')
elif sexo == 'F':
    print('Você não precisa realizar o alistamento.')
else:
    print('Sexo inválido.')
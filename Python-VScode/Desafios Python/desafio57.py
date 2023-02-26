sexo = str
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo (F/M): ')).strip().upper()[0]
    if sexo != 'F' and sexo != 'M':
        print('Sexo inválido. Por favos informe seu sexo.')
print(f'Sexo [{sexo}] registrado com sucesso.')

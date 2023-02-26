maior18 = mens = minas20 = int(0)
while True:
    print('-' * 20)
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: (F/M) ')).strip().upper()[0]
    while sexo not in ('FM'):
        sexo = str(input('Digite seu sexo: (F/M) ')).strip().upper()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        mens += 1
    if sexo == "F" and idade < 20:
        minas20 += 1
    print('Usuário cadastrado com sucesso.')
    print('-' * 20)
    resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    while resp not in ('SN'):
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if resp == 'N':
        break
print('=' * 20, 'FIM DO PROGRAMA', '=' * 20)
print(f'Total de pessoas com mais de 18 anos: [{maior18}].')
print(f'Ao todo temos [{mens}] homens cadastrados.')
print(f'E temos [{minas20}] com menos de 20 anos.')

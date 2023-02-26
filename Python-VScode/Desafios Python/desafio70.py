preço = totp = baratp = float(0.0)
mil = c = int(0)
nome = barato = str('')
while True: 
    print('-' * 30)
    nome = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço do produto: R$'))
    totp += preço
    if preço > 1000:
        mil += 1
    if c == 0:
        c += 1
        baratp = preço
        barato = nome
    if baratp > preço:
        baratp = preço
        barato = nome
    print('Produto registrado com sucesso.')
    print('-' * 30)
    resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if resp not in ('SN'):
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total de compra foi de [{totp:.2f}].')
print(f'Temos [{mil}] produtos que custam mais de R$1000.00')
print(f'O produto mais barato foi [{barato}], custando R$[{baratp}]')
    
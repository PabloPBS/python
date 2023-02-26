vel = int(input('Digite a velociade do veículo: '))
multa = (vel-80)*7
if vel > 80:
    print('Veículo multado.')
    print(f'Valor da multa: R${multa:.2f}')
else:
    print('Dentro do limite de velocidade. Continue assim.')
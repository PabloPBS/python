dist = float(input('Digite a distância da viagem, em Km: '))
if dist < 200:
    preco = 0.50*dist
else:
    preco = 0.45*dist
print(f'O preço da passagem será de R${preco:.2f}')
    
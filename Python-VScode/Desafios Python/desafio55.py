maior = float(0.0)
menor = float(0.0)
for c in range (0,5):
    if c == 1:
        menor = peso
    peso = float(input('Digite seu peso em Kg: '))
    if peso > maior:
        maior = peso
    if menor > peso:
        menor = peso
print(f'Maior peso digitado: {maior}KG.')
print(f'Menor peso digitado:{menor}KG.')
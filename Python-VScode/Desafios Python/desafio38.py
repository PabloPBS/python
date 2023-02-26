num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite segundo valor: '))
if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
else:
    print('Nenhum valor é maior ou menor, os dois são iguais.')
print(f'Valores digitados: {num1} e {num2}')
    
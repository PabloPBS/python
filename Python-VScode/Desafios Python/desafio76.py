t = ('Lápis' , 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*35)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('-'*35)
for c in range (0,len(t)):
    if c % 2 == 0:
        print(f'{t[c]:.<25}', end='')
    else:
        print(f'R${t[c]:>8}')
print('-'*35)

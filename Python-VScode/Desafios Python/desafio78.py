lista = []
for c in range(0,5):
    lista.append(int(input(f'Dijite o número da posição {c}: ')))
print('-=-'*13)
print(f'Maior valor digitado: [{max(lista)}].')
print(f'Posição do maior valor: [{lista.index(max(lista))}]')
print(f'Menor valor digitado: [{min(lista)}].')
print(f'Posição do menor valor: [{lista.index(min(lista))}]')
print(f'Lista: {lista}')

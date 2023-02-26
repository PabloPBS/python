lista = []
while True:
    resp = str(' ')
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? (S/N) ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Resposta inválida. Digite S ou N: ')).strip().upper()
    if resp == 'N':
        break
print(f'Lista de valores digitados: {lista}')
print(f'Quantidade de valores digitados: [{len(lista)}].')
print(f'Lista ordenada em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição [{lista.index(5)}].')
else:
    print('O valor 5 não foi digitado.')

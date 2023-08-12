lista = []

#Lendo entradas
for c in range(0,5):
    lista.append(int(input(f'Dijite o número da posição {c}: ')))
print('-=-'*13)

#Identificando o maior e menor valor da lista
for c in range(0,5):
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

#Identificando a posição do menor e maior valor
posMaior = []
posMenor = []
for i, v in enumerate(lista):
    if v == maior:
        posMaior.append(i)
    if v == menor:
        posMenor.append(i)

#Exibindo resultados
print(f'Lista: {lista}')
print(f'Maior valor digitado: [{maior}].')
print(f'Posição do maior valor: {posMaior}')
print(f'Menor valor digitado: [{menor}].')
print(f'Posição do menor valor: {posMenor}')

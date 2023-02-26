lista = []
aux = 0
for c in range(0,5):
    if lista[c] < lista[c+1]:
        lista.insert(int(input(f'Digite o {c+1}º valor: ')))
print(lista)
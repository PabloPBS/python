resp = str()
media = float(0)
maior = int(0)
menor = int(0)
c = int(0)
while resp != 'N':
    N = int(input('Digite um valor inteiro: '))
    c += 1
    resp = str(input('Deseja continuar? (S/N): ')).upper()
    media = media+N
    m = media/c
    if c == 1:
        menor = N
        maior = N
    if menor > N:
        menor = N
    if maior < N:
        maior = N
print(f'Soma de todos os valores digitados: {media}.')
print(f'A média entre todos os [{c}] valores é igual a [{m:.3f}].')
print(f'Maior valor digitado: {maior}')
print(f'Menor valor digitado: {menor}')

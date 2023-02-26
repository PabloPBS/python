media = float(0)
vei = int(0)
nova = int(0)
for c in range (1,5):
    print(f'------------ {c}ª PESSOA ------------')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo (M/F): ').upper()
    media = media + idade
    if idade > vei and sexo == 'M':
        vei = idade
        vei2 = (nome)
    if idade < 20 and sexo == 'F':
        nova = nova+1
media = media/4
print(f'Média de idade do grupo: {media:.2f}')
print(f'Nome do homem mais velho: {vei2}, com {vei} anos.')
print(f'Quantidade de mulheres com menos de 20 anos: {nova}')

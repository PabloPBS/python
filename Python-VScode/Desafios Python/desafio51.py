Primeiro = int(input('Digite o primeiro termo da Progressão Aritmética: '))
Razão = int(input('Digite a razão da PA: '))
for c in range (1,11):
    print(f'{c}º termo: {Primeiro}')
    Primeiro += Razão
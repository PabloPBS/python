n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+n2)/2
if m < 5:
    print('REPROVADO.')
    print(f'Média: {m:.1f}')
elif m > 5 and m < 7:
    print('RECUPERAÇÃO')
    print(f'Média: {m:.1f}')
else:
    print('APROVADO')
    print(f'Média: {m:.1f}')

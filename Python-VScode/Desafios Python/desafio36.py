val = float(input('Digite o valor do imóvel: R$'))
sal = float(input('Digite o salário do comprador: R$'))
tem = int(input('Digite em quantos anos o valor será pago: '))
prestação = val/(tem*12)
print(f'Para pagar uma casa de R${val:.2f} em {tem} anos, a prestação será de {prestação:.2f} por mês.')
if prestação > (0.3 * sal):
    print('Infelizmente você não pode financiar este imóvel.')
    print('Empréstimo Negado.')
else:
    print('Empréstimo Aprovado.')
    print('Tenha um bom dia.')

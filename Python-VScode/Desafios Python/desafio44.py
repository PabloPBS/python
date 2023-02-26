preço = float(input('Digite o preço do produto: R$'))
opção = int(input('Qual a opção de pagagento? \n 1 - À vista no dinheiro/cheque; \n 2 - À vista no cartão; \n 3 - Em 2x no cartão; \n 4 - Em 3x ou mais no cartão. \n Escolha: '))
if opção == 1:
    preço = preço-(preço * 0.1)
elif opção == 2:
    preço = preço-(preço * 0.05)
elif opção == 4:
    preço = preço+(preço * 0.2)
    par = int(input('Em quantas parcelas?'))
    par1 = preço/par
    print(f'Sua compra será parcelada em {par}x de R${par1:.2f} COM JUROS.')
print(f'Valor a pagar pelo produto: R${preço:.2f}')
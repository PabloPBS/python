sal = float(input('Digite o salário do funcionário: R$'))
if sal > 1250:
    nsal = sal*1.1
else:
    if sal <= 1250:
        nsal = sal*1.15
print(f'O novo salário será de R${nsal:.2f}.')

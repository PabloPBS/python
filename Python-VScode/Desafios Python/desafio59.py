from time import sleep
esc = int(0)
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
while esc != 5:
    print('---------- MENU ----------')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior Valor')
    print('[4] Digitar Novos Números')
    print('[5] Sair do Programa')
    esc = int(input('ESCOLHA: '))
    if esc == 1:
        print('O valor da soma é:', num1+num2)
    if esc == 2:
        print('O valor da multiplicação é:', num1*num2)
    if esc == 3:
        if num1>num2:
            print(f'O valor [{num1}] é maior.')
        else:
            print(f'O valor [{num2}] é maior.')
    if esc ==4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
    if esc not in (1,2,3,4,5):
        print('Opção inválida. Tente novamente.')
    sleep(1)
print('Programa Finalizado.')

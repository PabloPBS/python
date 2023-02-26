Num = int(input('Digite um número: '))
divs = int(0)
for c in range (1,Num+1):
    if Num % c == 0:
        divs = divs+1
        print ('\033[33m', end='  ')
    else:
        print ('\033[31m', end='  ',)
    print(c, end='  ')
print(f'\n \033[m O número [{Num}] foi divisível [{divs}] vezes.')
if divs == 2:
    print(f'\n\033[32m  O número [{Num}] É PRIMO!')
else:
    print(f'\n\033[31m  O Número [{Num}] NÃO É PRIMO!')
    
num1 = int(0)
num2 = int(1)
num3 = int(0)
c = int(0)
resp = int(input('Deseja ver quantos elementos da sequência de Fibonacci? '))
print(num1, end=' > ')
while c != resp:
    num1 = num2
    num2 = num3
    num3 = num1+num2
    print(f'{num3} > ', end='')
    c += 1
print('FIM!')

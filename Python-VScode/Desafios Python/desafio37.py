num = int(input('Digite um número inteiro: '))
con = int(input('Escolha a base de conversão: \n 1 - Binário \n 2 - Octal \n 3 - Hexadecimal \n 4- Todos \n Escolha: '))
if con == 1:
    print(f'{num} em binário é: ', bin(num)[2:])
elif con == 2:
    print(f'{num} em octal é: ', oct(num)[2:])
elif con == 3:
    print(f'{num} em hexadecimal é: ', hex(num)[2:])
elif con == 4:
    print(f'{num} em binário é: ', bin(num)[2:])
    print(f'{num} em octal é: ', oct(num)[2:])
    print(f'{num} em hexadecimal é: ', hex(num)[2:])
else: 
    print('Escolha inválida.')
print('-='*15)
print('    ANALISADOR DE TRIÂNGULOS')
print('-='*15)
a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))
if  abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('Com os valores fornecidos, um triângulo pode ser formado.')
else:
    print('Com os valores fornecidos, um triângulo não pode ser formado.')
    
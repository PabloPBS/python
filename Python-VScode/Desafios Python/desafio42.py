l1 = float(input('Valor do primeiro lado: '))
l2 = float(input('Valor do segundo lado: '))
l3 = float(input('Valor do terceiro lado: '))
if (l1 - l2) < l3 < (l1+l2) and (l1 - l3) < l2 < (l1+l3) and (l2 - l3) < l1 < (l2+l3):
    if l1 == l2 and l2 == l3:
        tipo = str('equilátero')
    elif l1 == l2 or l2 == l3 or l3 == l1:
        tipo = str('isóceles')
    elif l1 != l2 and l2 !=l3:
        tipo = str('escaleno')
    print(f'Um triângulo {tipo} pode ser formado.') 
else:
    print('Um triângulo não pode ser formado.')
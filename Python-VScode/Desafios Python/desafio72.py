nums = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
resp = str('S')
while resp == 'S':
    esc = int(input('Digite um número entre 0 e 20: '))
    while esc < 0 or esc > 20:
        esc = int(input('Valor inválido. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {nums[esc]}.')
    resp = str(input('Deseja continuar? (S/N) ')).strip().upper()

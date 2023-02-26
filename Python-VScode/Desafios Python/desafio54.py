import datetime
maiori = int(0)
menori = int(0)
for c in range (1,8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = int(datetime.datetime.today().year - nasc)
    if idade >= 21:
        maiori = maiori + 1
    else:
        menori = menori + 1 
print(f'Quantidade de pessoas QUE ATINGIRAM a maioridade: {maiori}.')
print(f'Quantidade de pessoas QUE NÃO ATINGIRAM a maioridade: {menori}.')

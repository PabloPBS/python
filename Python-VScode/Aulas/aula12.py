nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome Bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro':
    print ('Seu nome é bem popular no Brasil!')
elif nome == 'Ana' or nome == 'Claúdia' or nome == 'Jéssica' or nome == 'Juliana':
    print('Belo nome feminino!')
else:
    print ('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')

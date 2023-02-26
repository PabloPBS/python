frase = str(input('Digite uma frase: '))
frase = (frase.split())
frase = (''.join(frase))
frase = frase.lower()
verso = (frase[::-1])
verso = verso.lower()
if frase == verso:
    print('A frase que você digitou É um palíndromo.')
else:
    print('A frase que você digitou NÃO é um palíndromo.')

print(f'O inverso de {frase.upper()} é ', verso.upper())
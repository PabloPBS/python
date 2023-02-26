c = int(0)
end = int(10)
pri = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
print(pri, end=' > ')
while c != end:
    prox = pri + raz
    pri = prox
    print(prox, end=' > ')
    c += 1
    if c == end:
        resp = int(input('Deseja ver mais temros da PA? (Digite 0 para cancelar.) '))
        if resp != 0:
            end = end + resp
print(f'Programa encerrado. Foram fornecidos {c} termos da PA.')

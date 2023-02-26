from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(n)
print('O maior valor sorteado foi: ', max(n))
print('O menor valor sorteado foi: ', min(n))

'''from random import randint
n1 = n2 = n3 = n4 = n5 = menor = maior = int(0)
for c in range(1,6):
    if c == 0:
        menor = t[c]
        maior = t[c]
    n1 = randint(0,10)
    n2 = randint(0,10)
    n3 = randint(0,10)
    n4 = randint(0,10)
    n5 = randint(0,10)
t = (n1,n2,n3,n4,n5)
print(t)'''
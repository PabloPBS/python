val = int(input('Digite um número e você verá sua tabuada: '))
for c in range (1,11):
    resp = val*c
    print(f'{val} x {c:2}: {resp:3}')
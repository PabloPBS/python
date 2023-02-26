n = s = c = int(0)
while True:
    n = int(input('Digite um valor inteiro (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados [{c}] valores, e o resultado da soma de todos eles é [{s}].')

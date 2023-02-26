nums = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
noves = int(0)
pares = int(0)
par2 = int(0)
print(f'Você digitou os valores {nums}')
if 9 in nums:
    print(f'O valor [9] apareceu [{nums.count(9)}] vezes.')
else:
    print('Nenhum [9] foi digitado.')
if 3 in nums:
    print(f'O valor [3] apareceu na {nums.index(3)+1}ª posição.')
else:
    print('Nenhum valor [3] foi digitado.')
print('Os valores pares são: ', end='')
for c in range(0,4):
    if nums[c] % 2 == 0:
        print(nums[c], end='  ')


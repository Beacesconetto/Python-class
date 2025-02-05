x = int(input('Digite um número: '))
total = 0
for i in range(1, x):
    if x % i == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')
print(f'\n\033[mO número {x} foi dividido {total} vezes.')        
if total == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')
cont = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

if 9 in cont:
    print(f'O 9 apareceu {cont.count(9)} vezes')
else:
    print('O 9 não aparece nenhuma vez')    
if 3 in cont:    
    print(f'O primeiro 3 pareceuna posição {cont.index(3)}')
else:
    print('O 3 não aparece nenhuma vez')
print('Os núemros pares digitados são: ', end='')
for n in cont:
    if n % 2 == 0:
        print(f'{n} ', end='')

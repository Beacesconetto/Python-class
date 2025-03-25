numeros = list()
for cont in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'O maior valor digitado foi {max(numeros)} nas posições ', end='')
for x,y in enumerate(numeros): 
    if y ==  max(numeros):
        print(f'{x}    ', end= '')

print(f'\nO menor valor digitado foi {min(numeros)} nas posições ', end='')
for x,y in enumerate(numeros): 
    if y ==  min(numeros):
        print(f'{x}    ', end= '')
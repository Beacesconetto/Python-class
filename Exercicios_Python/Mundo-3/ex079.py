numeros = list()
while True:
    n = (int(input('Digite um valor: ')))    
    if n not in numeros:  
        numeros.append(n)
        print('Valor adicionado com sucesso!!!')
    else:
        print('Valor já existe na lista. Tente outro.')    
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        print('Resposta inválida. Digite apenas S ou N.')

    if resp == 'N':
        break

print(f'Você digitou os valores {sorted(numeros)}')

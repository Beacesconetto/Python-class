lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        print('Resposta inválida. Digite apenas S ou N.')
    if resp == 'N':
        print(f'Você digitou {len(lista)} elementos')
        lista.sort(reverse=True)
        print(f'Os valores em ordem decrescente são: {lista}')
        if 5 in lista:
            print('O valor 5 faz parte da lista')
        else:
            print('O valor 5 não faz parte da lista')    
        break

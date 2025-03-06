import random

total = v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0,10)
    total = jogador + computador
    tipo = ' '
    par = total % 2 == 0
    impar = total % 2 == 1
    while tipo not in 'IP':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} e ', end= '')
    print(' DEU PAR' if par else ' DEU ÍMPAR')    
    if tipo == 'P':
        if par :
            print('Você venceu!')
            v += 1
        else:
            print ('Você perdeu') 
            break   
    elif tipo == 'I':
        if impar :
            print('Você venceu!')
            v += 1
        else:
            print ('Você perdeu')
            break
    print('Vamos jogar de novo...')
print(f'GAME OVER! Você venceu {v} vezes')            

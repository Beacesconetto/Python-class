import random

item = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)

print('Vamos jogar Jokenpô!')
print(''''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('''    JO
    KEN
    PÔ''')

print('-' * 11)
print(f'Computador jogou {item[computador]}')
print(f'Jogador jogou {item[jogador]}')
print('-' * 11)

if computador == 0: 
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE')
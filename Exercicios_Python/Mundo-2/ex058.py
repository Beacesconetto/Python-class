import random

computador = random.randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

tentativas = 0
acertou = False

while not acertou:
    jogador = int(input('Qual o seu palpite: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
        print(f'Acertou com {tentativas} tentativas. Parabéns!')    
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
  
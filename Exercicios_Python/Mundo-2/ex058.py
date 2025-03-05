import random

computador = random.randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

tentativas = 0
acertou = False

while not acertou:
    num = int(input('Qual o seu palpite: '))
    tentativas += 1
    if num == computador:
        acertou = True
        print(f'Acertou com {tentativas} tentativas. Parabéns!')    
    else:
        if num < computador:
            print('Mais... Tente mais uma vez.')
        elif num > computador:
            print('Menos... Tente mais uma vez.')
  
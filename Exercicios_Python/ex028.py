import random
import time

computador = random.randint(0, 5)
num = int(input('Digite um número entre 0 e 5: '))
print('-' * 30)
print('Sorteando um número entre 0 e 5...')
print('-' * 30)
time.sleep(2) # Espera 2 segundos até rodar o próximo comando
if num == computador:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou! O número era {}'.format(computador))    
vel = float(input('Qual é a velocidade atual do carro? '))

if vel <=200:
    print('Você está prestes a começar uma viagem de {:.2f}Km/h'.format(vel))
    print('E o preço da sua passagem será de R${:.2f}'.format(vel*0.50))
else:
    print('Você está prestes a começar uma viagem de {:.2f}Km/h'.format(vel))
    print('E o preço da sua passagem será de R${:.2f}'.format(vel*0.45))
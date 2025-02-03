vel = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.2f}Km/h'.format(vel))

if vel <=200:
    print('E o preço da sua passagem será de R${:.2f}'.format(vel*0.50))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(vel*0.45))

"""
Maneira simplificada
preço = vel * 0.50 if vel <= 200 else vel * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
"""
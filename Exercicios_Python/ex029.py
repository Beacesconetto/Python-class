vel = float(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print('MULTAdo! Você excedeu o limite de velocidade que é de 80km/h.') 
    print ('O valor da multa é R${:.2f}'.format((vel - 80) * 7))
else:
    print('Você está dentro do limite de velocidade. Dirija com segurança e tenha um bom dia!')
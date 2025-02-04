dias=int(input('Quantos dias alugados? '))
km=float(input('QUantos Km rodados? '))
dinheiro= dias*60 + 0.15*km
print('O total a pagar é {:.2f}' .format(dinheiro))
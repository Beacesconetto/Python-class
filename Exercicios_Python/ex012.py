n1=float(input('Qual o preço do produto? R$'))
p=n1-(n1*5/100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar {:.2f}' .format(n1,p))
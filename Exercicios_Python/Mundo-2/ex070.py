print('-' * 40)
print('           LOJA SUPER BARATÃO')
print('-' * 40)
total = caro = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do prouto: ')).strip()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    resp = ' '
    if preco >= 1000:
        caro += 1
    if cont == 1 or preco < menor:  
        menor = preco
        barato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print(f'O total da compra foi R${total:.2f}')
        print(f'Temos {caro} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {barato} que custa R${menor}')
        break
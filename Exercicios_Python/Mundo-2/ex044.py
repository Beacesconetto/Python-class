preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')     
lista = []
par = lista[:]
impar = lista[:]
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
for x,y in enumerate(lista):
    if y % 2 == 0:
        par.append(y)
    else:
        impar.append(y)    
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')

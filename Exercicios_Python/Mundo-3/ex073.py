time = ('Atlético-MG', 'Bahia', 'Botafogo', 'Ceará SC', 'Corinthias', 'Cruzeiro', 'Flamengo', 'Fluminence','Fortaleza', 'Grêmio', 'Internacional', 'Juventude','Mirassol', 'Palmeiras', 'Bragantino', 'Santos', 'Sport Recife', 'São Paulo', 'Vasco', 'Vitória')

print(f'Os 5 primeiros são: {time[0:5]}')
print('-' * 85)
print(f'Os 4 últimos são: {time[-4:]}')
print('-' * 85)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-' * 85)
print(f'O Flamengo está na {time.index('Flamengo')+ 1} posição')
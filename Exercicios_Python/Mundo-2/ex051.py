print('=' * 41)
print('          10 TERMOS DE UMA PA')
print('=' * 41)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print(c, end=' -> ')
print('FIM')
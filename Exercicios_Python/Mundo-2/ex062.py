print('=' * 41)
print('              Gerador de PA')
print('=' * 41)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')    
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')
    
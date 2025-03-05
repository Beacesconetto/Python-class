print('='*40)
print('              BANCO CEV')
print('='*40)
sacar = int(input('Que valor você quer sacar: R$'))


ced50 = sacar // 50
resto = sacar % 50
if ced50 > 0:
    print(f'Total de {ced50} cédulas de 50')

ced20 = resto // 20
resto = resto % 20
if ced20 > 0:
    print(f'Total de {ced20} cédulas de 20')  

ced10 = resto // 10
resto = resto % 10
if ced10 > 0:
    print(f'Total de {ced10} cédulas de 10')  

ced1 = resto // 1
resto = resto % 1
if ced1 > 0:
    print(f'Total de {ced1} cédulas de 1')          

'''
SOLUÇÃO ALTERNATIVA USANDO WHILE:


print('='*40)
print('              BANCO CEV')
print('='*40)
sacar = int(input('Que valor você quer sacar: R$'))
total = sacar
ced = 50
totced = 0
while True:
    if total >= ced:
       total -+ced
       total += 1
    else:
        if totced > 0:
            print(f'O total de {totced} cédulas de RS{ced}')
        if ced == 50:
            ced == 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break              


'''
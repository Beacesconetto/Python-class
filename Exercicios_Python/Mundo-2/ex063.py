print('~' * 41)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 41)
t0 = 0
t1 = 1
print(f'{t0} -> {t1}', end= '')
cont = 3

while cont <= n:
    t2 = t0 + t1
    print(f' -> {t2}', end= '')
    t0 = t1
    t1 = t2
    cont += 1
print(' -> FIM')
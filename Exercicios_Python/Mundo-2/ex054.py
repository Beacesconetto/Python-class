from datetime import date
maior = 0
menor  = 0
for i in range(1, 8):
    ano = int(input('Digite em que ano a pessoa nasceu: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')    
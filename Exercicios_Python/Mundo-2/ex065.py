resp = 'S'
cont = total = menor = maior = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    total += num
    cont += 1
    if cont == 1:
         maior = menor = num
    else: #Fazer assim ao inves de só com elif garante que  verifique se o num > maior e num < menor porem com o elif ele verifica um mas não o outro 
        if num > maior:
              maior = num
        if num < menor:
             menor = num

    resp = str(input('Quer continuar? [S/N]')).strip().upper()
media = total/cont        
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

    

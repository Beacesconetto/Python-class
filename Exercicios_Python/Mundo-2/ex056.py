menor20 = 0
maisVelho = 0
somaIdade = 0
media  = 0
nomeMaisVelho = ''
for x in range (1, 5):
    print(f'----- {x}ª PESSOA -----')
    nome = str(input(f'Digite o nome da {x}ª pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {x}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {x}ª pessoa [F/M]: ')).strip().upper()
    somaIdade += idade
    if idade < 20 and sexo == 'F':
        menor20 += 1
    if x == 1 and sexo == 'M':
        maisVelho = idade
        nomeMaisVelho = nome
    elif sexo == 'M' and  idade > maisVelho:
        maisVelho = idade
        nomeMaisVelho = nome

media = somaIdade / 4
print(f'A média de idade do grupo é de {media} anos.')    
print(f'{menor20} mulheres tem menos de 20 anos.')
print(f'O homem mais velho é {nomeMaisVelho} e tem {maisVelho} anos.')   
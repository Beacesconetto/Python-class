totalM = mais18 = menos20 = 0

while True:
    print('-' * 30)
    print('    CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
        if sexo == 'M':
            totalM += 1
        if idade >= 18:
            mais18 += 1   
        if sexo == 'F' and idade < 20:
            menos20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print(f'Total de pessoas com mais de 18 anos: {mais18}')
        print(f'Ao todo temos {totalM} homens cadastrados')
        print(f'E temos {menos20} mulheres com menos de 20 anos')
        break
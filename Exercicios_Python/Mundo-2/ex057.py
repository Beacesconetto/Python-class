sexo = str(input('Informe seu sexo: [M/F]  ')).strip().upper()[0] 
# [0] para pegar a primeira letra da string

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')    
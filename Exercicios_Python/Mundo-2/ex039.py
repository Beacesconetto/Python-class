import datetime

ano = int(input('Digite o seu ano de nascimento: '))
idade = datetime.datetime.now().year - ano

if idade < 18:
    print(f'Você ainda vai se alistar no serviço militar, faltam {18 - idade} anos.')
elif idade == 18:
    print('Está na hora de se alistar no serviço militar.')
else:   
    print(f'Você já passou do tempo de se alistar no serviço militar, passaram-se {idade - 18} anos.')        

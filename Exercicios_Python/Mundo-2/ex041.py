import datetime

ano = int(input('Digite o seu ano de nascimento: '))
idade = datetime.datetime.now().year - ano
print(f'Você tem {idade} anos.')
if idade <= 9:
    print('Portanto você é um atleta da categoria MIRIM.')
elif idade <= 14:
    print('Portanto você é um atleta da categoria INFANTIL.')
elif idade <= 19:
    print('Portanto você é um atleta da categoria JUNIOR.')
elif idade <= 25:
    print('Portanto você é um atleta da categoria SÊNIOR.')
else:
    print('Portanto você é um atleta da categoria MASTER.')        
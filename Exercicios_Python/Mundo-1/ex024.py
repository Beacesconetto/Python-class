# Crie um pragrama que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTo

cidade = str (input("Em que cidade você nasceu? ")).strip()
print(cidade[:5].upper() == 'SANTO')


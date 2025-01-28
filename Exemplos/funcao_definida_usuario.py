def calcular_media(*numeros):  # O asterisco indica que numeros será uma tupla contendo todos os valores passados para a função
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("A média é: ", calcular_media(10, 20, 30))
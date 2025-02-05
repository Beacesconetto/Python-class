frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(len(junto))
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
        print('A frase é um palíndromo!')
else:   
        print('A frase não é um palíndromo!')
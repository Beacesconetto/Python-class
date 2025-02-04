print('-' * 20)
print('Analisador de Triângulos')
print('-' * 20)
a = float(input('Digite o valor do primeiro segmento: '))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
    if a == b == c:
        print('O triângulo é EQUILÁTERO!')
    elif a != b != c: # Pode ser feito assim também:  a == b or a == c or b == c
        print('O triângulo é ISÓSCELES!')
    else:
        print('O triângulo é ESCALENO!')        
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')    
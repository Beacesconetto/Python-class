num = 0
total = 0
cont = 0
# Forma simplificada -> num = cont = total = 0
while num != 999:
    total += num
    cont += 1
    num = int(input('Digite um número ou 999 para parar: '))
print(f'Você digitou {cont} números e a soma entre eles foi {total}')
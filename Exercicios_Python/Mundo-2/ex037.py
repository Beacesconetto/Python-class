num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [1] converter para BINÁRIO
      [2] converter para OCTAL
      [3] converter para HEXADECIMAL''')
inp = int(input('Sua opção: '))

# binario = format(num, 'b')outrro método para converter para binário (b) octal (o) e hexadecimal (x)
if inp == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}') # [2:] remove os dois primeiros caracteres 0b indica que o número está em base binária.
elif inp == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif inp == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:      
    print('Opção inválida! Tente novamente.')        
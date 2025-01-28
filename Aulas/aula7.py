# // divisão inteira (5//2==2)
# % resto da divisão (5//2==1)
# pow() potencia porem perder na ordem 
n1=int(input('Digite um número '))
n2=int(input('Digite outro número '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {} \n o produto é {} e a dvisão é {:.2f}' .format(s, m, d), end=' ')
print('Divisão inteira {} e a potência {}' .format(di, e))
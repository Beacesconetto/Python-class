n1=int(input('Digite um número para ver sua tabuada: '))
n2 = int(input('Digite o número final da tabuada: '))

for c in range(1,n2+1):
    print(f'{n1} x {n2} = {n1*c}')
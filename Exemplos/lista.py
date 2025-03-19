num = [2, 5, 9, 1]
num[2] = 3 #Subistitui o elemento 2 por 3

num.append(7) #Adiciona 7 a lista
print(num)

num.sort(reverse=True) #Organiza do maior para o menor
print(num)

print(f'Essa lista tem {len(num)} elementos')

num.insert(2,2) #Na posição 2 inseri o número 0 e "empurra" os outros números para frente
print(num)

num.pop(0) #Elimina um elemento. Se estiver sem um elemento especifico apaga o último da lista
print(num)

num.remove(2) #Remove a primeira ocorrencia de um elemento
print(num)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')


valores = []
valores.append(5)
valores.append(9)
valores.append(7)

for c,v in enumerate(valores): #Enumerate pega a posição e o elemento da lista
    print(f'Na posição {c} encontrei o valor {v}!')

numeros = list()
for cont in range(0,5):
    numeros.append(int(input('Digite um valor: ')))
    
for x,y in enumerate(numeros): 
    print(f'Na posição {x} encontrei o valor {y}!')    

a = [2, 3, 4, 7]
b = a[:] #Se estiver assim se eu mudar algo na lista B a lista A não muda 
b[2] = 8 #Muda as duas listas se b = a
print(f'Lista A {a}') 
print(f'Lista B {b}')    
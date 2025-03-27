lista = []

for c in range(5):
    n = int(input("Digite um valor: "))
    
    # Se for o primeiro número ou se for maior que o último da lista
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista!!!')
    else:
        for x, y in enumerate(lista):
            if n <= y:  
                lista.insert(x, n)
                print(f'Adicionado na posição {x}!!!')
                break

print("Lista ordenada:", lista)



'''
lista = []  
for c in range(0,5): 
    n = int(input("Digite um valor: ")) 
    print(lista)
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1    
print("Lista ordenada:", lista) 
'''



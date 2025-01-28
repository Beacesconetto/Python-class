frutas = ["maçã", "banana", "laranja"]


frutas.append("pera")
print(frutas)  # adiciona um elemento ao final da lista.


frutas.insert(1, "uva")
print(frutas)  # insere um elemento em uma posição específica da lista.


frutas.remove("banana")
print(frutas)  # remove a primeira ocorrência de um elemento na lista.


fruta_removida = frutas.pop(2)
print(frutas)  # remove e retorna o elemento em uma posição específica da lista.
print(fruta_removida)  # Imprime a fruta que foi removida que seria "laranja"


frutas.sort()
print(frutas)  # ordena os elementos da lista em ordem ascendente.

frutas.reverse()
print(frutas)  # inverte a ordem dos elementos na lista.
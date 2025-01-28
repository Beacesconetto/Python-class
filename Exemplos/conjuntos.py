# Para criar um conjunto pode se utilizar chaves ou a função set():

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

# Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  


intersecao = conjunto1 & conjunto2
print(intersecao)  


diferenca = conjunto1 - conjunto2
print(diferenca)  


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)


frutas.add("pera")
print(frutas)  # adiciona um elemento ao conjunto.


frutas.remove("banana")
print(frutas)  # remove um elemento do conjunto. Se o elemento não existir, gera um erro.


frutas.discard("uva")
print(frutas)  # remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.


frutas.clear()
print(frutas)  # remove todos os elementos do conjunto.
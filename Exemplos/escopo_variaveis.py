def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  
funcao2()  
print(variavel_global)  
# print(variavel_local) Gera um erro, a variável não está definida neste escopo.
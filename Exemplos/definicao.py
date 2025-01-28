# Para definir uma função em Python, se usa o def seguida do nome da função e parênteses. Opcionalmente, podemos especificar parâmetros dentro dos parênteses. 

def saudacao():
    print("Olá, mundo!")

saudacao()  

def saudacao2(nome):
    print(f"Olá, {nome}!") # o f indica que tem uma variavel que nesse caso seria nome

saudacao2("João")  
saudacao2("Maria")

idade = 23
altura = 1.75
nome = "Beatriz"
status = True

print(f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.")

# funções podem retornar valores usando o return.

def soma(a, b):
    return a + b

resultado = soma(3, 4)
print(resultado)  
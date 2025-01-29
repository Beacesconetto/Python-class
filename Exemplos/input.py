nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))


print("Olá, " + nome + "!")

if idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade.")
else:
    print(f"Você Você tem {idade} anos e é menor de idade.")
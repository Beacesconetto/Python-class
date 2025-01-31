"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = str(input("Digite seu nome completo: ")).strip().split() #  Divide a string em uma lista de palavras, usando espaços como separador.
print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}" .format(nome[0])) # pega o primeiro elemento da lista
print("Seu último nome é {}" .format(nome[-1])) # pega o último elemento da lista

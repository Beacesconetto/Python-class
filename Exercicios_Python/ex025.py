# Criei um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome dela

nome = str (input("Digite seu nome completo: ")).strip()
print("O seu nome tem Silva? {}" .format('silva' in nome.lower()))

expressao = (str(input('Digite uma expressão: ')))
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':   
        if len(pilha) > 0:
            pilha.pop() #remove o último elemento de uma lista
        else:
            pilha.append(')')
            break   
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão não está válida')              
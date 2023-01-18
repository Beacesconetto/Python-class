salario=float(input('Qual é o salário do Funcionário? R$'))
aumento = salario + (salario*15/100)
print('Um funcionário que ganhava {}, com 15% de aumento, passa a receber {:.2f}'.format(salario,aumento))
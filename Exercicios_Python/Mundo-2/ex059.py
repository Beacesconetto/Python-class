import time

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0

while opcao != 5:
    print('''        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos números
        [5] Sair do programa      
        ''')
    opcao = int(input('>>> Qual a sua opção:  '))
    print('-' * 20) 
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Finalizando...')
        time.sleep(2)
    else:
        print('Opção inválida, tente novamente.')
    print('-' * 20) 
print('Fim do programa! Volte sempre!')
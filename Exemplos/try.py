# O bloco try contém o código que pode gerar uma exceção. 
# Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

try:
    sub = 10 - 2
    print(sub)

    resultado = 10 / 0  
    print(resultado)

    soma = 10 + 3
    print(soma)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido") 

# O bloco except especifica o tipo de exceção que se deseja capturar e lidar.
# Pode ter mais de um except para lidar com diferentes tipos de exceções.     


try:
    arquivo = open("arquivo.txt", "r")
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close() 

# O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não.
# É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.
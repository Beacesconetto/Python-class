import random
import datetime
import math
from modulo_personalizado import saudar

resultado = math.sqrt(25)
print(resultado)  

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) 


data_atual = datetime.datetime.now()
print(data_atual) 

saudar("João")
# seria assim se usasse o import geral -> resultado = modulo_personalizado.calcular_soma(5, 3)
# print(resultado)


"""
Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.

from math import sqrt


resultado = sqrt(25)
print(resultado) 

"""
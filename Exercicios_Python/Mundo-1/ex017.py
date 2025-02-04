'''from math import sqrt
cat1=float(input('Comprimento do cateto oposto: '))
cat2=float(input('Comprimento do cateto adjacente: '))
H=sqrt(cat1**2+cat2**2)
print('A hipotenusa vai medir {:.2f}'.format(H))'''

import math
co=float(input('Comprimento do cateto oposto: '))
ca=float(input('Comprimento do cateto adjacente: '))
hi=math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}' .format(hi))
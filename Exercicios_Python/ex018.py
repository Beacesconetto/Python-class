import math
an=float(input('Digite o ângulo que você deseja: '))
seno=math.sin(math.radians(an))
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))
print('O ânguo de {} tem o SENO de {:.2f}'.format(an,seno))
print('O ângulo de {} tem o COSSENO {:.2f}'.format(an,cos))
print('O ângulo de  {} tem a TANGENTE {:.2f}' .format(an,tan))
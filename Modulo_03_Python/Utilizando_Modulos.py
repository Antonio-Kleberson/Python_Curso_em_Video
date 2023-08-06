#importando a biblioteca matematica
import math

num = int(input('Digite um numero: '))
#utilizando a biblioteca para calcular raiz quadrada
raiz = math.sqrt(num)
#aredondando o numero para cima
print('A raiz quadrada de {} é: {}'.format(num, math.ceil(raiz)))
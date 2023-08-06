import math

n1 = float(input('Informe o cateto oposto: '))
n2 = float(input('Informe o cateto adjacente: '))

Co = math.pow(n1, 2)
Ca = math.pow(n2, 2)

soma = Co + Ca
hip = math.sqrt(soma)

print('A hipotenusa do triangulo é: {:.2f}'.format(hip))

#Tambem poderia ser resolvido da seguinte forma:
#hip = (Co ** 2 + Ca ** 2) ** (1/2)
#Ou da seguinte forma e mais resumida:
#hip = math.hypot(n1, n2)
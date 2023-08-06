import math

ang = float(input('Digite um angulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno do angulo é: {:.2f}'.format(sen))
print('O cosseno do angulo é: {:.2f}'.format(cos))
print('A tangente do angulo é: {:.2f}'.format(tan))
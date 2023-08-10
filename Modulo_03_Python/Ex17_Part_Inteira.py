#Crie um programa que receba um numero quebrado e mostre apenas a parte inteira.
#Ex: 6.127 = 6
#Ex: 6.999 = 6


from math import trunc

num = float(input('Digite um numero quebrado: '))

print('A parte inteira do numero digitado é: {}'.format(trunc(num)))

#pode utilizar tambem o int(num), assim nao precisa de modulos
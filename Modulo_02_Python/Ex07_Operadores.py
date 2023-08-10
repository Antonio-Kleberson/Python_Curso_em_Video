#Crie um programa que receba um numero e calcule o seu dobro, triplo e a raiz quadrada.

n1 = int(input('Digite um numero: '))

d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print('O dobro de {} é: {}'.format(n1, d))
print('O triplo de {} é: {}'.format(n1, t))
print('A raiz de {} é: {:.2f}'.format(n1, r))

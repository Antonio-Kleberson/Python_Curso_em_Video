#Crie um programa que receba um numero e mostre seu antecessor e sucessor.

n1 = int(input('Digite um numero: '))

ant = n1 - 1
suc = n1 + 1

print('O antecessor de {} é: {}'.format(n1, ant))
print('O sucessor de {} é: {}'.format(n1, suc))
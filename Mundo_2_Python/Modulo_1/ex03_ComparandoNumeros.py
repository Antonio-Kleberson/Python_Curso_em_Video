# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor valor e maior
# O segundo valor e maior
# Nao existe valor maior, os dois sao iguais

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um segundo numero inteiro: '))

if num1 > num2:
    print('O primeiro valor {} é maior'.format(num1))
elif num2 > num1:
    print('O segundo valor {} é maior'.format(num2))
else:
    print('Os dois valores {} e {} são iguais!'.format(num1, num2))
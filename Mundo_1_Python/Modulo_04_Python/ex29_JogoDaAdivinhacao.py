#Escreva um programa que faca o computador pensar em um numero inteiro entre 0 e 5, e peca para o usuario descobrir qual foi o numero escolhido pelo computador. 
#O programa devera escrever na tela se o usuario venceu ou perdeu.

#Importar biblioteca para gerar numeros aleatorios inteiros
from random import randint

num = randint(0, 5)

print('O computador pensou em um numero entre 0 e 5. Tente adivinhar qual foi o numero escolhido pelo o computador')

numero = int(input('Digite um numero entre 0 e 5: '))

if numero == num:
    print('Parabens, voce acertou o numero escolhido pelo o computador')
else:
    print('Desculpe, mas voce errou o numero escolhido pelo o computador')
    print('O numero escolhido foi: {}'.format(num))
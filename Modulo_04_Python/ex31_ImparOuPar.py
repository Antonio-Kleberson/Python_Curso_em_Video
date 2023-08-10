#Crie um programa que leia um numero inteiro e diga se ele e impar ou par

num = int(input('Digite um numero inteiro: '))

res = num % 2 

if res == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))
#Crie um programa que leia tres numeros inteiros e diga qual e o maior e qual e o menor valor

n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
n3 = int(input('Digite o terceiro valor inteiro: '))

menor = n1
#Testando quem e menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Testando quem e maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
    
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
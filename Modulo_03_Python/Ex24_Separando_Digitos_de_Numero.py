#Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

numero = str(input("Digite o numero: "))

print('Unidade: {}'.format(numero.split()[3]))
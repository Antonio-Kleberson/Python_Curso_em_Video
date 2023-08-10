#Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

numero = str(input("Digite o numero: "))

print('Unidade: {}'.format(numero.split()[3]))
print('Dezena: {}'.format(numero.split()[2]))
print('Centena: {}'.format(numero.split()[1]))
print('Milhar: {}'.format(numero.split()[0]))
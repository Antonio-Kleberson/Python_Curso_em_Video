#Crie um programa que leia um nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite o nome da pessoa: ").upper()).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome))
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo sem considerar os espacos
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome completo em maiusculo: {}'.format(nome.upper()))
print('Seu nome completo em minusculo: {}'.format(nome.lower()))
print('Quantidade de letras sem considerar os espacos: {}'.format(len(nome) - nome.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(nome.find(' ')))

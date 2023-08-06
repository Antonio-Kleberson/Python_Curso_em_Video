#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo sem considerar os espacos
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))

print('Seu nome completo em maiusculo: {}'.format(nome.upper()))
print('Seu nome completo em minusculo: {}'.format(nome.lower()))
#Vai trocar os espacos e juntar as palavras
contar = len(nome.replace(" ", ""))
print('Quantidade de letras sem considerar os espacos: {}'.format(contar))
#Vai mostrar apenas o primeiro nome
primeiro_nome = nome.split()[0]
#Vai contar as letras do primeiro nome
print('Quantidade de letras do primeiro nome: {}'.format(len(primeiro_nome)))

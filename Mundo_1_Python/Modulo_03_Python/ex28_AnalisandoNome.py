#Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.

nome = str(input('Digite o nome da pessoa: '))

#Vai localizar o primeiro nome
print('Primeiro nome: {}'.format(nome.split()[0]))
#Vai localizar o ultimo nome
print('Ultimo nome: {}'.format(nome.split()[-1]))

#Crie um programa que receba duas notas e calcule a media.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2)/2

print('A media das notas {} e {} é: {:.2f}'.format(n1, n2, med))
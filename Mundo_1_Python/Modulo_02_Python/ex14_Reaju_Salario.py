#Crie um programa que receba o valor do salario e calcule o reajuste de 15%.

sal = float(input('Informe o seu salario: R$'))

aum = sal * 0.15
novosal = sal + aum

print('O seu novo salario vai ser: R${:.2f}'.format(novosal))
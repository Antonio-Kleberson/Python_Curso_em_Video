#Escreva um programa que pergunte o salario do funcionairo e calcule o valor do aumento.
#Para salarios superiores a R$1.250,00, calcule um aumento de 10%.
#Para salarios inferiores a R$1.250,00, cdalcule um aumento de 15%.

sal = float(input('Informe o seu salario: R$'))

if sal > 1250:
    aumento = sal * 0.1
    novsal = aumento + sal
    print('Seu novo salario vai ser de: R${:.2f}'.format(novsal))
else:
    aumento = sal * 0.15
    novsal = aumento + sal
    print('Seu novo salario vai ser de: R${:.2f}'.format(novsal))
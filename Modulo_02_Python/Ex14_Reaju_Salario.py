sal = float(input('Informe o seu salario: R$'))

aum = sal * (15 / 100)
nsal = sal + aum

print('O seu novo salario vai ser: R${:.2f}'.format(nsal))
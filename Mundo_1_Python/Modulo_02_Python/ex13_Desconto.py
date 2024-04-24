#Crie um programa que receba um preco de um produto e calcule o preco do desconto.

preco = float(input('Informe o preço do produto: '))
desc = float(input('Informe o desconto: '))

valor = preco * (desc / 100)
novp = preco - valor

print('O novo preco do produto vai ser: R${:.2f}'.format(novp))
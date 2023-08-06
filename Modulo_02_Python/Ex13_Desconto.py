preco = float(input('Informe o preço do produto: '))
desc = float(input('Informe o desconto: '))

valor = preco * (desc / 100)
novp = preco - valor

print('O novo preco do produto vai ser: R${:.2f}'.format(novp))
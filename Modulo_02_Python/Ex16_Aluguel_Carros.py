d = int(input('Quantos dias você alugou o carro: '))
km = float(input('Quantos quilometros você percorreu: '))

Td = d * 60
Tkm = km * 0.15

print('O valor total do aluguel é de {:.2f}'.format(Td + Tkm))
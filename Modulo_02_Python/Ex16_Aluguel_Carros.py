#Crie um programa que calcule o valor do aluguel de um carro com base na quantidade de dias e Km percorridos.
# Formula: Td = d * 60
# Formula: Tkm = km * 0.15
# Formula: T = Td + Tkm

d = int(input('Quantos dias você alugou o carro: '))
km = float(input('Quantos quilometros você percorreu: '))

Td = d * 60
Tkm = km * 0.15

print('O valor total do aluguel é de {:.2f}'.format(Td + Tkm))
#Crie um programa que receba um valor em reais e convertar para dolar, euro e libra.

valor = float(input('Quantos reais você tem? R$'))

dolar = valor / 4.86
euro = valor / 5.73
libra = valor / 6.71

print('Dolar: ${:.2f}\n Euro: €{:.2f}\n Libra: £{:.2f}'.format(dolar, euro, libra))
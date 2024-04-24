#Crie um programa que receba um valor em metros e converta para centimetros e milimetros.

n1 = float(input('Digite um valor em metros: '))

cm = n1 * 100
mm = n1 * 1000

print('O resultado em centimetro é: {:.2f}'.format(cm))
print('O resultado em milimetro é: {:.2f}'.format(mm))
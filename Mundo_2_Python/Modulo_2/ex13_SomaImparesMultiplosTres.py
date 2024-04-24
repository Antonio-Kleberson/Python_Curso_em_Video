#  Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
c = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        c += c
        soma += cont
print('A soma dos {} valores é {}.'.format(c, soma))
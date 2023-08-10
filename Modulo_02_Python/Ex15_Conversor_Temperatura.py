#Crie um programa que receba a temperatura em graus e converta ela para Kelvin e Fahrenheit.
# Formula: Tc = (Tf - 32) / 1.8
# Formula: Tc = Tk - 273
# Formula: Tf = (Tc * 1.8) + 32

Tc = float(input('Informe a temperatura em graus: '))

Tk = Tc + 273
Tf = (Tc * 1.8) + 32

print('A temperatura em Graus é: {:.2f} °C\n A temperatura em Kelvin é {:.2f} K\n A temperatura em Fahrenheit é: {:.2f} F'.format(Tc, Tk, Tf))
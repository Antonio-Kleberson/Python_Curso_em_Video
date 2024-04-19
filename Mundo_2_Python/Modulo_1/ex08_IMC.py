# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: ABAIXO DO PESO
# - Entre 18.5 e 24.9: PESO IDEAL
# - Acima de 25 ATE 30: ACIMA DO PESO
# - 30 ate 40: OBESIDADE
# - Acima de 40: OBESIDADE MORBIDA

peso = float(input('Informe o seu  peso em kg: '))
altura = float(input('Informe a sua altura em metros: '))

#  Cálculo do IMC é dado pela fórmula: (Peso / (Altura²))
imc = peso /  (altura ** 2)

if(imc < 18.5):
    print(f'Seu IMC é {imc:.1f}, você está ABAIXO DO PESO')
elif(imc > 18.5 and imc <= 24.9):
    print(f'Seu IMC é {imc:.1f}, você está no PESO IDEAL')
elif(imc > 25 and imc <= 30):
    print(f'Seu IMC é {imc:.1f}, você está ACIMA DO PESO')
elif(imc > 30 and imc <= 40):
    print(f'Seu IMC é {imc:.1f}, você está em OBESIDADE')
else:
    print(f'Seu IMC é {imc:.1f}, você está em OBESIDADE MORBIDA')
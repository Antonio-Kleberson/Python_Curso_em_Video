#Escreva um programa que leia a velocidade de um caro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#O motorista deve pagar R$07,00 por cada Km acima do limite

vel = int(input('Digite a velocidade do veiculo em Km/h: '))

if vel > 80:
    #Adicionando cores no terminal
    print('\033[1;30;41mVoce foi multado por ultrapassar a velocidade permitida!\033[m')
    multa = (vel - 80) * 7
    print('O valor da multa é de \033[1;31;43mR${:.2f}\033[m'.format(multa))
else:
    print('\033[1;30;42mVelocidade no limite permitido!\033[m')
    print('\033[1;30;44mTenha um bom dia! Dirija com segurança!\033[m')
#Desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preco da passagem, cobrando R$0,50 por Kmpara viagens de ate 200Km e R$0,45 para viagens mais longas

dist = int(input('Informe a distancia da viagem em Km: '))

if dist <= 200:
    preco = dist * 0.50
    print('Sua viagem de {}Km vai custar R${}'.format(dist, preco))
else:
    preco = dist * 0.45
    print('Sua viagem de {}Km vai custar R${}'.format(dist, preco))
# Crie um programa que faca o computador jogue Jokenpo

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('|----------|ESCOLHA UMA JOGADA|----------|')
print('|----------| [0] -    PEDRA   |----------|')
print('|----------| [1] -    PAPEL   |----------|')
print('|----------| [2] -    TESOURA |----------|')
print('|----------------------------------------|')

jogador = int(input('Qual a sua jogada: '))
print('-=' * 15)
print('O computador escolheu: {}'.format(itens[computador]))
print('O jogador escolheu: {}'.format(itens[jogador]))
print('-=' * 15)

if computador == 0: #Computador jogou Pedra
    if jogador == 0: #Jogador jogou Pedra
        print('EMPATE')
    elif jogador == 1: #Jogador jogou Papel
        print('JOGADOR VENCEU A PARTIDA')
    elif jogador == 2: #Jogador jogou Tesoura
        print('COMPUTADOR VENCEU A PARTIDA')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #Computador jogou Papel
    if jogador == 0: #Jogador jogou Pedra
        print('COMPUTADOR VENCEU A PARTIDA')
    elif jogador == 1: #Jogador jogou Papel
        print('EMPATE')
    elif jogador == 2: #Jogador jogou Tesoura
        print('JOGADOR VENCEU A PARTIDA')
    else:
        print('JOGADA INVALIDA')
elif computador == 2: #Computador jogou Tesoura
    if jogador == 0: #Jogador jogou Pedra
        print('JOGADOR VENCEU A PARTIDA')
    elif jogador == 1: #Jogador jogou Papel
        print('COMPUTADOR VENCEU A PARTIDA')
    elif jogador == 2: #Jogador jogou Tesoura
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')

print('-=' * 15)
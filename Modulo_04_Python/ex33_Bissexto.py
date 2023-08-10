#Crie um programa que leia um ano qualquer e determine se ele e bissexto
from datetime import date

ano = int(input('Digite um ano qualquer: '))

caso1 = ano % 4 
caso2 = ano % 100
caso3 = ano % 400

#Se o valor for 0, vai ser considerado o ano atual do computador
if ano == 0:
    ano = date.today().year
    print('O ano atual é {}'.format(ano))
if caso1 == 0 and caso2 != 0 or caso1 == 0 and caso2 == 0 and caso3 == 0:
    print('O ano de {} é Bissexto'.format(ano))
else:
    print('O ano de {} não é Bissexto'.format(ano))
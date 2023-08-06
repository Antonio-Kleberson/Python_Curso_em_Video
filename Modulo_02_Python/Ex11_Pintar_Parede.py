lar = float(input('Qual a largura da parede em Metros: '))
alt = float(input('Qual a altura da parede em Metros: '))

area = lar * alt
lit = area / 2

print('A área da parede é de {:.2f}m² e será necessário {:.2f} litros de tinta para pintá-la.'.format(area, lit))
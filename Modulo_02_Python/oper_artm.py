n = input('Qual e o seu nome? ')

#vai escrever o nome em 20 espacos
print('Prazer em te conhecer {:20}!' .format(n))
#vai escrever o nome 20 espacos depois
print('Prazer em te conhecer {:>20}!' .format(n))
#vai escrever o nome 20 espacos antes
print('Prazer em te conhecer {:<20}!' .format(n))
#vai escrever o nome no centro 
print('Prazer em te conhecer {:^20}!' .format(n))
#vai escrever o nome em 20 espacos, centralizado preenchido com sinal de igual
print('Prazer em te conhecer {:=^20}!' .format(n))
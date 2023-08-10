n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo valor: '))

# soma
s = n1 + n2
# subtracao
su = n1 - n2
# multiplicacao
m = n1 * n2
# divisao
d = n1 / n2
# divisao inteira
di = n1 // n2
# exponeciacao
e = n1 ** n2

# {:.3f} indica formatacao das casas decimais
# \n faz quebra de linha, end='' junta os prints na mesma linha
print('A soma é {}\n a subtração é {}\n a multiplicação é {}\n a divisão é {:.3f}\n' .format(s,su,m,d))
print('A divisão inteira é {}\n a exponeciação é {}\n' .format(di, e))


#-------------------------------------------------------------------------------------------------------
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
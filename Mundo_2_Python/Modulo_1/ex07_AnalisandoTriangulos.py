# Refaca o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# - Equilatero: Todos os lados iguais
# - Isoceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes


r1 = float(input('Informe a primeira reta: '))
r2 = float(input('Informe a segunda reta: '))
r3 = float(input('Informe a terceira reta: '))

#A Desigualdade Triangular: Para um triângulo ser possível, a soma de quaisquer dois lados do triângulo deve ser sempre maior que o terceiro lado.
c1 = r1 + r2
c2 = r1 + r3 
c3 = r2 + r3

if c1 > r3 and c2 > r2 and c3 > r1:
    print('As retas informadas podem formar um triangulo!')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3:
        print('ESCALENO')
    elif r1 == r2 != r3:
        print('ISOCELES')
else:
    print('As retas informadas não podem formar um triangulo!')
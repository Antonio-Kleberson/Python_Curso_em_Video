# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao:
# 1 para binario
# 2 para octal
# 3 para hexadecimal


num = int(input("Digite um número inteiro: "))

print('_______________________________________________')
print('-----------------------------------------------')
print('Escolha uma das opções para realizar a conversão')
print('-----------------------------------------------')
print('| 1 - Converter para Binário     |')
print('| 2 - Converter para Octal       |')
print('| 3 - Converter para Hexadecimal |')
opcao = int(input('Digite a opção desejada para conversão: '))
print('_______________________________________________')

if opcao == 1:
    binario = ''
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num = num // 2
    print(f'O número em binário é {binario}')
elif opcao == 2:
    print(f'O número em octal é {oct(num)}')
elif opcao == 3:
    print(f'O número em hexadecimal é {hex(num)}')
else:
    print('Opção inválida.')

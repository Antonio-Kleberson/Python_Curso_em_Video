# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
# - A vista Dinheiro/Pix: 10% de desconto
# - A vista no Cartao: 5% de desconto
# - Em ate 2x no Cartao: Preco normal
# - 3x ou mais no Cartao: 20% de juros


print("Escolha um produto:")
print("|---------------------------|")
print("| 1 - Celular    |R$ 1000,00|")
print("| 2 - TV 32'     |R$ 1500,00|")
print("| 3 - Geladeira  |R$ 2500,00|")
print("| 4 - Fogão      |R$ 2100,00|")
print("| 5 - Computador |R$ 2000,00|")
print("|---------------------------|")
opcao = int(input("Digite  o numero da opção: "))

preco = 0

if(opcao == 1):
    preco = 1000
elif(opcao == 2):
    preco = 1500
elif(opcao == 3):
    preco = 2500
elif(opcao == 4):
    preco = 2100
elif(opcao == 5):
    preco = 2000
else:
    print("Opção Invalida!!")
    
print("Escolha uma opção de pagamento:")
print("|------------------------------------------------|")
print("| 1 - Dinheiro ou PIX           |  10% Desconto  |")
print("| 2 - À vista no cartão         |  5% Desconto   |")
print("| 3 - Em ate 2x no cartão       |  Sem Desconto  |")
print("| 4 - Em 3x ou  mais no cartão  |  20 de Juros   |")
print("|------------------------------------------------|")
pagamento = int(input("Digite o número da opção: "))

valor = 0

if(pagamento == 1):
    valor = preco - (preco * 0.1)
elif(pagamento == 2):
    valor = preco - (preco * 0.05)
elif(pagamento == 3):
    valor = preco 
elif(pagamento == 4):
    valor = preco + (preco * 0.2)
else:
    print("Opção Invalida!!")
    
print("O produto escolhido foi:  ", end=" ")
if(opcao == 1) :
    print("Celular)", end=" ")
elif(opcao == 2):
    print("TV 32", end=" ")
elif(opcao == 3):
    print("Geladeira", end=" ")
elif(opcao == 4):
    print("Fogão", end=" ")
else:
    print("Computador", end=" ")

print("\nValor do produto: R$ {:.2f}".format(valor))

    
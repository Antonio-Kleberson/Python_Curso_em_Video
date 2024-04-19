# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.

valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salario do comprador: "))
qnt_anos = int(input("Informe em quantos anos vai pagar: "))

valor_parcelas = valor_casa / (qnt_anos * 12)

if(valor_parcelas > (salario * 0.3)):
    print("-----------------------------------------------")
    print("Emprestimo negado!")
    print("Valor da parcela muito alta pro salario determinado!")
    print("-----------------------------------------------")
else:
    print("-----------------------------------------------")
    print("Parabens! Emprestimo concedido!")
    print("Valor da Casa: {}".format(valor_casa))
    print("Valor da Parcela: {:.2f}".format(valor_parcelas))
    print("Quantidade de anos para pagar: {} meses ({} anos)".format((qnt_anos * 12), qnt_anos))
    print("-----------------------------------------------")

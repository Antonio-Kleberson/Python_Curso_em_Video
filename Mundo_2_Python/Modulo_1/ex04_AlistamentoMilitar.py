# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao servico militar.
# - Se e a hora de se alistar.
# - Se ja passou do tempo de alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que faltou do prazo.

from datetime import date

def alistamento(ano_nasc):
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    
    if idade < 18:
        print("Voce não tem idade de alistamento!")
        print(f"Ainda faltam {18 - idade} anos para completar")
    elif idade == 18:
        print("Já é hora de fazer o alistamento")
    else:
        print("Já passou do tempo de alistamento.")

ano_nasc = int(input("Informe a data de nascimento: "))
alistamento(ano_nasc)
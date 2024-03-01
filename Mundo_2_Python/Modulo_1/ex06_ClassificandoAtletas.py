# A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Ate 9 anos: MIRIM
# - Ate 14 anos: INFANTIL
# - Ate 19 anos: JUNIOR
# - Ate 20 anos: SENIOR
# - Acima: MASTER


from datetime import datetime


def categoria(nasc):
    data_atual = datetime.now()

    # Calculando a diferença entre a data atual e a data de nascimento
    dif = data_atual - nasc

    # Obtendo a parte de anos da diferença
    idade = dif.days // 365
    
    print("\n")
    
    if idade <= 9:
        print("CATEGORIA: MIRIM")
    elif idade <= 14:
        print("CATEGORIA: INFANTIL")
    elif idade <= 19:
        print("CATEGORIA: JUNIOR")
    elif idade <= 20:
        print("CATEGORIA: SENIOR")
    else:
        print("CATEGORIA: MASTER")
        
    print("\n")
    
dia = int(input("Informe o dia do nacimento: "))
mes = int(input("Informe o mes do nacimento: "))
ano = int(input("Informe o ano do nacimento: "))

nasc = datetime(ano, mes, dia)
categoria(nasc)

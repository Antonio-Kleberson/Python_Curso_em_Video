#Calcular consumo mensal de racao
def consumo_mensal(qnt_animais, kg_racao, kg_saco):
    consumo_diario = qnt_animais * kg_racao
    consumo_mes = consumo_diario * 30
    qnt_sacos = consumo_mes / kg_saco
    
    return consumo_diario, consumo_mes, qnt_sacos 

# Path: Projeto_Praticos/calcular_racao.py

def main():
    qnt_animais = int(input('Informe a quantidade de animais: '))
    kg_racao = float(input('Informe o consumo de um unico animal no dia: '))
    kg_saco = float(input('Informe o quantos Kg tem um saco de ração: '))
    
    valores = (qnt_animais, kg_racao, kg_saco)
    
    consumo = consumo_mensal(*valores)
    
    consumo_diario, consumo_mes, qnt_sacos = consumo_mensal(*valores)
    
    print('------------------------------------------------------')
    print(f'O consumo diário foi de: {consumo_diario} kg por dia.')
    print(f'O consumo mensal foi de: {consumo_mes} kg por mês.')
    print(f'Quantidade de sacos necessários foi de: {qnt_sacos}')
    print('------------------------------------------------------')
    

# Verifica se este arquivo está sendo executado diretamente como um programa principal.
if __name__ == "__main__":
    # Chama a função 'main' para iniciar o programa.
    main()
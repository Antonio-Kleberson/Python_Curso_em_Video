#Calcular consumo mensal de racao
def consumo_mensal(qnt_animais, kg_racao, kg_saco):
    consumo_diario = qnt_animais * kg_racao
    consumo_mes = consumo_diario * 30
    qnt_sacos = consumo_mes / kg_saco
    
    return consumo_diario, consumo_mes, qnt_sacos 

def racao_crescimento(qnt_racao):
    milho = 0.72
    soja = 0.24
    nucleo = 0.04
    
    qnt_milho = qnt_racao * milho
    qnt_soja = qnt_racao * soja
    qnt_nucleo = qnt_racao * nucleo
    
    qnt_total = qnt_milho + qnt_soja + qnt_nucleo
    
    return qnt_milho, qnt_soja, qnt_nucleo, qnt_total

def racao_terminacao(qnt_racao):
    milho = 0.76
    soja = 0.20
    nucleo = 0.04
    
    qnt_milho = qnt_racao * milho
    qnt_soja = qnt_racao * soja
    qnt_nucleo = qnt_racao * nucleo
    
    qnt_total = qnt_milho + qnt_soja + qnt_nucleo
    
    return qnt_milho, qnt_soja, qnt_nucleo, qnt_total

def racao_gestacao(qnt_racao):
    milho = 0.57
    soja = 0.09
    trigo = 0.30
    nucleo = 0.04
    
    qnt_milho = qnt_racao * milho
    qnt_soja = qnt_racao * soja
    qnt_trigo = qnt_racao * trigo
    qnt_nucleo = qnt_racao * nucleo
    
    qnt_total = qnt_milho + qnt_soja + qnt_trigo + qnt_nucleo
    
    return qnt_milho, qnt_soja, qnt_trigo, qnt_nucleo, qnt_total

def racao_lactacao(qnt_racao):
    milho = 0.59
    soja = 0.24
    trigo = 0.09
    nucleo = 0.04
    
    qnt_milho = qnt_racao * milho
    qnt_soja = qnt_racao * soja
    qnt_trigo = qnt_racao * trigo
    qnt_nucleo = qnt_racao * nucleo
    
    qnt_total = qnt_milho + qnt_soja + qnt_trigo + qnt_nucleo
    
    return qnt_milho, qnt_soja, qnt_trigo, qnt_nucleo, qnt_total

# Path: Projeto_Praticos/calcular_racao.py

def main():
    qnt_animais = int(input('Informe a quantidade de animais: '))
    kg_racao = float(input('Informe o consumo de um unico animal no dia: '))
    kg_saco = float(input('Informe o quantos Kg tem um saco de ração: '))
    
    valores = (qnt_animais, kg_racao, kg_saco)
    
    consumo = consumo_mensal(*valores)
    
    consumo_diario, consumo_mes, qnt_sacos = consumo_mensal(*valores)

    qnt_milho, qnt_soja, qnt_nucleo, qnt_total = racao_crescimento(consumo_mes)
    
    print('------------------------------------------------------')
    print(f'O consumo diário foi de: {consumo_diario} kg por dia.')
    print(f'O consumo mensal foi de: {consumo_mes} kg por mês.')
    print(f'Quantidade de sacos necessários foi de: {qnt_sacos}')
    print('------------------------------------------------------')
    print('Quantidade de milho utilizado: {:.2f}'.format(qnt_milho))
    print('Quantidade de soja utilizado: {:.2f}'.format(qnt_soja))
    print('Quantidade de nucleo utilizado: {:.2f}'.format(qnt_nucleo))
    print('Total: {:.2f}'.format(qnt_total))
    

# Verifica se este arquivo está sendo executado diretamente como um programa principal.
if __name__ == "__main__":
    # Chama a função 'main' para iniciar o programa.
    main()
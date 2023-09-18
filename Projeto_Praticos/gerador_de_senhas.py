# Escreva um programa que solicite ao usuário uma senha e verifique se ela atende a certos critérios, como comprimento mínimo, uso de letras maiúsculas e minúsculas e números.

import random
import string

def gerar_senha(comp, letras=True, numeros=True, simbolos=True):
    # Inicializa uma string vazia chamada 'caracteres' para armazenar os caracteres que comporão a senha.
    caracteres = ''
    
    # Verifica se 'letras' é True e, se for, adiciona todas as letras maiúsculas e minúsculas à variável 'caracteres'.
    if letras:
        caracteres += string.ascii_letters
    # Verifica se 'numeros' é True e, se for, adiciona todos os dígitos à variável 'caracteres'.
    if numeros:
        caracteres += string.digits
    # Verifica se 'simbolos' é True e, se for, adiciona todos os símbolos à variável 'caracteres'.
    if simbolos:
        caracteres += string.punctuation
    # Se 'caracteres' ainda estiver vazio após as verificações, retorna uma mensagem de erro.
    if not caracteres:
        return "Nenhum tipo de caractere selecionado para a senha"
    
    # Gera a senha propriamente dita:
    # - Utiliza um loop for para criar uma sequência de caracteres aleatórios com o comprimento desejado.
    # - 'random.choice(caracteres)' seleciona aleatoriamente um caractere de 'caracteres' em cada iteração.
    # - Usa 'join' para unir esses caracteres em uma única string, que é armazenada na variável 'senha'.
    senha = ''.join(random.choice(caracteres) for _ in range(comp))
    
    # Retorna a senha gerada.
    return senha

def main():
    print('-------------------------------------')
    print('GERADOR DE SENHAS')
    print('-------------------------------------')
    
    # Informar o comprimento da senha a ser gerada
    comp = int(input('Digite o comprimento da senha: '))
    # Informar se a senha vai ter letras
    letras = input('Sua senha deve conter letras? (sim/não): ').lower() == 'sim'
    # Informar se a senha vai ter numeros
    numeros = input('Sua senha deve conter numeros? (sim/não): ').lower() == 'sim'
    # Informar se a senha vai ter simbolos
    simbolos = input('Sua senha deve conter simbolos? (sim/não): ').lower() == 'sim'
    
    # Chama a funcao gerar_senha e passa as variaveis como parametros 
    senha = gerar_senha(comp, letras, numeros, simbolos)
    
    print(f"Sua senha é: {senha}")

# Verifica se este arquivo está sendo executado diretamente como um programa principal.
if __name__ == "__main__":
    # Chama a função 'main' para iniciar o programa.
    main()
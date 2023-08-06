# Manipulando texto

frase = 'Curso em Vídeo Python'

# FATIAMENTO
# Vai localizar o caractere no espaco 9
print(frase[9])
# Vai localizar o caractere no espaco 9 e 13
# O retorno sempre será o ultimo espaco -1
print(frase[9:13])
# Vai exibir a frase a partir do nove ate o final, mas pulando em dois e dois
print(frase[9:21:2])
# Vai exibir a frase desde o caractere 0 ate a posicao 5
print(frase[:5])
# Vai exibir a frase da posicao 15 ate o final
print(frase[15:])
# Vai exibir de 9 ate o final, mas vai pulando 3 posicoes
print(frase[9::3])

# ANALISE
# Vai mostrar o comprimento da frase
print(len(frase))
# Vai contar quantas vezes aparece determinada caractere
print(frase.count('o'))
# Vai realizar um fatiamento, e depois vai contar quantas vezes essa caractere aparece nesse fatiamento
print(frase.count('o', 0, 14))
# Vai dizer em que momento comecou o conjunto de caracteres
print(frase.find('deo'))
# Quando ele procurar por uma palavra que nao existe, vai retornar -1
print(frase.find('bola'))
# Vai retornar true ou false de acordo com a afirmacao
print('Curso' in frase)

# TRANSFORMACAO
# Vai trocar a palavra dentro da frase
print(frase.replace('Python', 'Android'))
# Vai deixar a frase em maiuscula
print(frase.upper())
# Vai deixar a frase em minuscula
print(frase.lower())
# Vai deixar tudo em minusculo, com execao da letra da primeira palavra
print(frase.capitalize())
# Vai analisar cada palavra, e vai deixar a primeira letra em maiuscula
print(frase.title())
# Vai remover os espacos excedentes, n o inicio e no final da string
print(frase.strip())
# Vai remover somente os espacos da direita
print(frase.rstrip())
# Vai remover somente os espacos da esquerda
print(frase.lstrip())

# DIVISAO
# Vai dividir a frase em uma lista, separando cada palavra
# Nessa divisao, a contagem de cada palavra reinicia
print(frase.split())

# JUNCAO
# Vai juntar a frase, mas vai colocar o caractere que eu quiser entre cada palavra
print('-'.join(frase))

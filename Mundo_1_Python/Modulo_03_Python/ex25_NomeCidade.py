#Crie um programa que leia o nome da cidade e diga se ela começa com a palavra "SANTO".

cidade = str(input("Digite o nome da cidade: ")).strip()
#Strip remove os espaços em branco do início ou no final.

print(cidade[:5].upper() == 'SANTO')
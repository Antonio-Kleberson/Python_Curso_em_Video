# Crie um programa que leia duas notas de um aluno e calcule sua media. Mostrando uma mensagem no final, de acordo com a media atingida:
# - Media abaixo de 5.0: REPROVADO
# - Media entre 5.0 e 6.9: RECUPERADO
# - Media acima de 7.0: APROVADO

qnt = int(input("Quantas notas você quer informar: "))
notas = []

# Adicionando notas ao vetor
for i in range(qnt):
    nota = float(input("Informe a {}° nota: \n".format(i+1)))
    notas.append(nota)

print("\n")

# Media das notas
media = sum(notas) / qnt

# Imprimindo as notas sem colchetes
print("Notas:", end=" ")
for nota in notas:
    print(nota, end=" | ")

print("\n")

print("MÉDIA: {}".format(media))
if media < 5:
    print("\n\nA sua média é {:.1f} e você está REPROVADO.".format(media))
elif media <= 6.9:
    print("\n\nA sua média é {:.1f} e você está em RECUPERAÇÃO.".format(media))
else:
    print("\n\nA sua média é {:.1f} e você está APROVADO.".format(media))
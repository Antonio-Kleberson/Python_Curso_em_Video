#Faça um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra "A"
#Em que posicao ela aparece a primeira vez
#Em que posicao ela aparece a ultima vez

frase = str(input('Digite uma frase: ').upper()).strip()

#Count vai contar quantas vezes a palavra se repete
print('Quantas vezes aparece a letra A')
print(frase.count('A'))
#Vai dizer em que momento apareceu a letra A
print('Primeira posicao da letra A')
print(frase.find('A'))
#Vai indicar o momento que aparece a ultima vez
print('Ultima posicao da letra A')
print(frase.rfind('A'))
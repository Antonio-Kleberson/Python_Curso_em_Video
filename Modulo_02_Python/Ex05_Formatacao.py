v = input('Digite algo: ')

#verifica o tipo da variavel
print('O tipo primitivo desse valor é: ', type(v))
#verifica se tem somente espaços
print('So tem espaços? ', v.isspace())
#verifica se é um numero
print('É um numero? ', v.isnumeric())
#verifica se é alfabetico
print('É alfabetico? ', v.isalpha())
#verifica se tem letras e numeros
print('Tem letras e numeros? ', v.isalnum())
#verificar se esta em letras maisucula
print('Esta em letras maisuculas? ', v.isupper())
#verificar se esta em letras minusculas
print('Esta em letras minusculas? ', v.islower())
#verificar se esta capitalizada
print('Esta capitalizada? ', v.istitle())
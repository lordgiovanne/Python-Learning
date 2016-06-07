#Primeiro definimos uma string para trabalharmos e a armazenamos na variavel texto
texto = "Hello World!"

#   Funcao que retorna o numero de caracteres em uma string ("len(nome_da_string)"):
print len(texto)        #imprime o valor retornado, ou seja, "12"
soma = len(texto) + 3   #cria uma variavel soma de tipo inteiro e armazena o valor 12+3=15
print "%d" %soma        #imprime o valor inteiro contido em soma, ou seja, "15"

#   Funcao que retorna o indice em que aparece pela primeira vez uma certa "substring" na string maior, lembre-se queo indice do 
#primeiro caractere e 0 ("nome_da_string.index("substring")"):
print texto.index("o")  #imprime o indice em que aparece pela primeira vez a letra o, ou seja, "4"
produto = texto.index("rl")*len(texto)   #cria uma variavel de tipo inteira chamada produto e armazena o valor 8*12=96
print "%d" %produto     #imprime o valor inteiro contido em produto, ou seja, "96"


print texto.count("l")
print texto[0:4]
print texto[::-1]
print texto.upper()
print texto.lower()
separar = texto.split(" ")
print "%s" % separar
#comentar e explicar

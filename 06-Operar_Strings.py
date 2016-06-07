#Primeiro definimos uma string para trabalharmos e a armazenamos na variavel texto
texto = "Hello World!"

#   Funcao que retorna o numero de caracteres em uma string ("len(nome_da_string)"):
print len(texto)        #imprime o valor retornado, ou seja, "12"
soma = len(texto) + 3   #cria uma variavel soma de tipo inteiro e armazena o valor 12+3=15
print "%d" %soma        #imprime o valor inteiro contido em soma, ou seja, "15"

#   Funcao que retorna o indice em que aparece pela primeira vez uma certa "substring" na string maior, lembre-se queo indice do 
#primeiro caractere e 0 ("nome_da_string.index("substring")"):
print texto.index("o")  #imprime o indice em que aparece pela primeira vez a letra o, ou seja, "4"
produto = texto.index("rl")*len(texto)    #cria uma variavel de tipo inteira chamada produto e armazena o valor 8*12=96
print "%d" %produto     #imprime o valor inteiro contido em produto, ou seja, "96"

#   Funcao que retorna o numero de vezes em que determinada "substring" aparece na string maior ("nome_da_string.count("substring")"):
print texto.count("l")  #imprime o numero de vezes que o caractere l aparece em texto, ou seja, "3"
divisao = texto.count("l")/2.0            #cria a variave real chamada divisao e armazena o valor 3/2.0=1.5
print "%.1f" %divisao   #imprime o valor real armazenado em divisao com uma casa decimal, ou seja, 1.5


print texto[0:4]
print texto[::-1]
print texto.upper()
print texto.lower()
separar = texto.split(" ")
print "%s" % separar
#comentar e explicar

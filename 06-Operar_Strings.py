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

#   Funcao que retorna um conjunto de caracteres selecionados a partir da string inicial. A chamada e feita na sintaxe 
#("nome_da_string[start:stop:step]"), de forma que os caracteres retornados sao aqueles que possuirem indice entre start-1 e stop
#e satisfizerem a relacao indice=start+k*step, onde k assume todos os naturais. 
print texto[0:4:1]      #imprime todos os caracteres cujo indice esta entre -1 e 4 e satisfaz indice=0+k*1, ou seja, os indices 
#0,1,2 e 3 e a funcao print imprime "Hell"
print texto[0:4]        #quando o step vale 1, pode nao escreve-lo, deixando-o subentendido, dessa forma sera impresso "Hell"
WtH = "What the " + texto[0:4] + "?"    #cria uma string chamada WtH e armazena "What the Hell?" nela
print "%s" %WtH         #imprime o valor armazenado na string, ou seja, "What the Hell?"
#Pode-se inverter uma string inteira utilizando a sintaxe ("nome_da_string[::-1]")
print texto[::-1]       #imprime a string texto de tras para frente, ou seja, "!dlroW olleH"

#   Funcao que retorna a string com os caracteres todos em maiusculo ou minusculo ("nome_da_string.upper()") para maiusculo e 
#("nome_da_string.lower()") para minusculo, perceba que nao sao utilizados parametros alem da propria string.
print texto.upper()     #imprime a string texto com todos os caracteres em maiusculo, ou seja, "HELLO WORLD!"
print texto.lower()     #imprime a string texto com todos os caracteres em minusculo, ou seja, "hello world!"
concatenado = texto.upper() + " " + texto.lower()   #cria uma variavel string que armazena os valores retornados pelas funcoes
#em questao separadas por espaco
print "%s" %concatenado #imprime o valor contido na string concatenado, ou seja, "HELLO WORLD! hello world!"


separar = texto.split(" ")
print "%s" % separar
#comentar e explicar

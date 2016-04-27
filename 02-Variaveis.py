#   Nesta parte do turorial iremos trabalhar com variaveis do tipo numero ou string. Em python, nao e necessario declarar variaveis, 
#visto que e uma linguagem orientada a objetos (discussao para outro momento).

#   Numeros serao classificados em dois tipos: inteiros ou fracionarios. Basta, portanto, atribuir valores as variaveis (que podem 
#receber qualquer nome nao reservado a linguagem e contendo os caracteres permitidos) e utiliza-las. Por ex:

a=5    #acabamos de atribuir o tipo inteiro para a variavel "a" e o valor 5
b=5.0  #acabamos de atribuir o tipo fracionario para a variavel "b" e o valor 5.0
c=float(7)  #tambem podemos atribuir o tipo fracionario dessa maneira!  

#   Strings sao conjuntos de caracteres e para atribuir o tipo string a uma variavel basta escrever o string desejado entre aspas
#duplas ou simples. No caso de atribuir com aspas simples, tome cuidado para nao utilizar apostrofes dentro da string. Ou, por
# padrão, atribua strings sempre usando aspas duplas e evite qualquer problema. Por ex:

d='nao posso usar apostrofes'
e="nao ' preciso ' mais ' me ' preocupar ' com ' apostrofes ' mal ' interpretados"

#   E possivel atribuir valores a mais de uma variavel ao mesmo tempo. Basta atribuir as com mesmo tipo na mesma linha e seus valores 
#devem estar de acordo, respectivamente, com suas chamadas. Por ex:

inteiro1, inteiro2 = 1,2
fracionario1, fracionario2 = float(1), 2.0
string1, string2 = "olar", "tchau"

#   Vamos verificar os valores atribuidos a cada variavel:

print "inteiro1 vale: %d" % inteiro1
print "inteiro2 vale: %d" % inteiro2
print "fracionario1 vale: %.1f" % fracionario1
print "fracionario2 vale: %.1f" % fracionario2
print "string1 contem: %s" % string1
print "string2 contem: %s" % string2

#   Para testar esse codigo, os posteriores e caso queira desenvolver e testar os proprios codigos, voce pode entrar no site 
#"http://learnpython.org/" digitar o código na code window e clickar em "run"

#Proximo asssunto: operadores

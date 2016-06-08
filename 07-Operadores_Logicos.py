#   Em python existem apenas dois valores logicos: True(verdadeiro/diferente de 0) e False(falso/igual a 0).
#Expressoes comparativas retornam valores logicos e esses, por sua vez, podem ser utilizados como condicao para a execucao de
#algum comando. 
#   Vamos utilizar as seguintes variaveis para os exemplos:
batman = 10
robin = 0
lista1 = [1,2,3]
lista2 = [15,2]

#   Os comparadores mais simples sao: igualdade(==), diferenca(!=), desigualdade simples(> e <) e desigualdades maior ou igual
#e menor ou igual(>= e <=).
print batman == 10      #imprime o valor logico retornado pela expressao, ou seja, "True", ja que 10=10
print robin != 0        #imprime o valor logico retornado pela expressao, ou seja, "False", ja que 0 nao e diferente de 0
print robin > batman    #imprime o valor logico retornado pela expressao, ou seja, "False", ja que 0 nao e maior que 10
print robin <= batman   #imprime o valor logico retornado pela expressao, ou seja, "True", ja que 0 e menor ou igual 10

#   Outros dois comparadores logicos muito utilizados sao o e(and) e ou(or). Estes servem, como sua intuicao deve estar dizendo-o
#justamente para relacionar o valor logico retornado por duas expressoes e gerar um novo valor logico.
print batman == 10 and robin != 0   #imprime "False", ja que a primeira parte da expressao retorna True e a segunda False
print batman == 10 or robin != 0    #imprime "True", ja que a primeira parte da expressao retorna True e a segunda False
#Para entender melhor os valores logicos retornados estude "logica booleana".

#   Comandos condicionais sao provavelmente o principio mais elementar e utilizado na programacao. Veremos, por enquanto os comandos:
#caso(if <condicao>:), senao caso(elif <condicao>:) e senao(else <nada>:). Esses comandos condicionais exigem uma identacao adequada,
#quando o valor logico retornado pela expressao condicional e True, os comandos no bloco abaixo sao executados e quando e False nao 
#sao (um bloco e definido pela sua identacao).
if batman > 8:          #os comandos no bloco abaixo sao exetados, ja que a expressao retorna "True"
  print "batman contem um valor maior do que oito"    #executa
if robin != 0:          #os comandos no bloco abaixo nao sao executados, ja que a expressao retorna "False"
  print "robin contem um valor diferene de zero"      #nao executa
elif  batman >= 10:     #os comandos no bloco abaixo sao exetados, ja que a expressao retorna "True"
  print "batman contem um valor maior ou igual a dez" #executa
else        #os comandos no bloco nao sao executados, pois a condicao do if referente a este else retorna "True"
  print "batman contem um valor menor que dez"

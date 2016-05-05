#   Operadores sao simbolos que promovem uma operacao. Na primeira parte deste tutorial iremos ver operadores com numeros.

#   Operadores aritmeticos:
#As operacoes basicas com numeros em python sao a soma (+), a subtracao (-), a multiplicacao (*), a divisao (/ ou //)¹, o
#modulo (%) e a potencia (**). 
#¹-A divisao com barra simples gera um resultado da divisao comum, por exemplo: 3.0/4.0=0.75. Porem,  quando os valores sao 
#todos inteiros, a barra simples executa a divisao inteira, ou seja: 3/4=0. A barra dupla e usada para se obter a divisao
#inteira independentemente dos tipos dos numeros operados, por exemplo: 3.0//4.0=0.

soma = 3+7.4
subtracao = 7-3
multiplicacao = 7*3
divisao1 = 7/2.0
divisao2 = 7/2
divisao3 = 7.5//3.0
modulo = 7%3
potencia = 7**2
print(soma)           #imprime "10.4"
print(subtracao)      #imprime "4"
print(multiplicacao)  #imprime "21"
print(divisao1)       #imprime "3.5"
print(divisao2)       #imprime "3"
print(divisao3)       #imprime "2.0"
print(modulo)         #imprime "1"
print(potencia)       #imprime "49"

#   Operadores com strings:
#O python tem a concatenacao de strings nativa. Ou seja, para "grudar" uma string na outra basta utilizar o operador (+).
#Por exemplo:

concatenacao = "olar" + " " + "amiguinhos" + "!"
print(concatenacao)   #imprime "olar amiguinhos!"

#A outra possivel operacao com strings e a repeticao. Basta utilizar o operador (*) e repetir uma string quantas vezes desejar.
#Por exemplo:

repeticao = "olar " * 3
print(repeticao)      #imprime "olar olar olar "

#   Operadores com listas:
#Assim como nas strings, e possivel "concatenar" duas listas ou repeti-la nvezes. Basta utilizar os mesmos operadores. Por ex:

lista1=[1,2]+[3,4,5]
print(lista1[0])      #imprime "1"
print(lista1[1])      #imprime "2"
print(lista1[2])      #imprime "3"
print(lista1[3])      #imprime "4"
print(lista1[4])      #imprime "5"
lista2=[3] * 5
print(lista2[0])      #imprime "3"
print(lista2[1])      #imprime "3"
print(lista2[2])      #imprime "3"
print(lista2[3])      #imprime "3"
print(lista2[4])      #imprime "3"

#Proximo assunto: formatacao de strings.

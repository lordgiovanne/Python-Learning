#   Quando se precisa imprimir o conteudo que esta armazenado em alguma variavel utilizam-se operadores de formatacao
#cada argumento (tipo de variavel ou lista) tem um operador adequado para se utilizar. Segue uma lista de operadores de
#formatacao basicos:
#"%s" - Listas no geral (lembrando que strings sao basicamente listas de caracteres) e numeros.
#"%d" - Uma maneira mais adequada para numeros inteiros.
#"%f" - Uma maneira mais adequada para numeros reais.
#"%.yf - Onde y e um numero natural que representa o numero de casas apos a virgula que se deseja imprimir.
#"%x ou %X - Imprime o numero desejado na base hexadecimal. (%x imprime as letras em minusculo)
#Exemplos(note que quando se deseja imprimir o valor contido em mais de uma variavel utiliza-se a notacao "% (var1, var2,...,varN)"

nome = "Wayne"
inteiro = 17
real = 3.141592
lista = [11, 2.718281, "Welcome home, Master"]
print "%s %s!" % (lista[2], nome)   #imprime "Welcome home, Master Wayne!"
print "Tenho %d anos." % inteiro    #imprime "Tenho 17 anos."
print "O numero pi vale %f, o numero de Euler vale %.3f nas tres primeiras casa decimais" % (real, lista[1])
#imprime "O numero pi vale 3.141592, o numero de Euler vale 2.718 nas tres primeiras casa decimais"
print "Os numeros %d e %d na base decimal equivalem aos numeros %X e %x na base hexadecimal" % (lista[0], inteiro, lista[0], inteiro)
#imprime "Os numeros 11 e 17 na base decimal equivalem aos numeros B e 11 na base hexadecimal"
print "A lista contem: %s" % lista  #imprime "A lista contem: [11, 2.718281, 'Welcome home, Master']"

#Proximo assunto: Operadores de strings.

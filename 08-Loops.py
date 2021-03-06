#   Muitas vezes voce ira se deparar com situacoes em que uma determinada acao deve aparecer repetidas vezes em seu codigo.
#Para evitar que voce tenha que escrever todas as vezes a mesma sentenca e para criar possibilidades de determinar o numero
#de vezes que esta sentenca e executada dinamicamente, existem os lacos de loop. Em python os lacos de loop sao o for e o 
#while.
#   Os lacos for e while sao definidos por identacao, assim como os comandos condicionais. 
#   O bloco de um for e realizado para cada valor que uma variavel auxiliar assume dentro de uma lista de valores. Para fazer 
#com que uma determinada variavel auxiliar adquira os valores de uma lista, podemos utilizar uma lista ou gerar uma atraves da
#funcao "xrange" que recebe como argumento "(start,stop,step)" de forma que os caracteres retornados sao aqueles que possuirem 
#indice entre start-1 e stop e satisfizerem a relacao indice=start+k*step, onde k assume todos os naturais.
lista = [0,3,7]
for x in lista:       #cria um laco no qual o bloco abaixo e executado para cada valor de x dentro da lista "lista"
  print x             #imprime o valor da variavel x, ou seja: 
#0
#3
#7
for i in xrange(3,8,2): #cria um laco no qual o bloco abaixo e executado para cada valor de x dentro da lista [3,5,7] retornada
  print i               #imprime o valor da variavel i, ou seja: 
#3
#5
#7
#   O bloco de um while e executado enquanto uma certa condicao retornar o valor True. Funciona como se fosse um if no qual a
#condicao e verificada sempre que acaba a execucao do bloco, "como se" existisse um comando implicito na ultima linha do bloco
#do if indicando para o programa que deve retornar a linha em que o if se encontra. Para evitar que o seu programa entre em
#loop, ou seja, execute o bloco infinitamente e nao continue para os proximos passos, e necessario alterar algum fator envolvido
#na condicao do while dentro do bloco de execucao.
j=0               #declara o inteiro j que assume o valor 0
while j < 4:      #executa o bloco abaixo enquanto o valor contido em j for menor que 4
  print j         #imprime o valor contido em j
  j=j+1           #aumenta em 1 o valor contido em j
#Ou seja, na primeira vez: testa se j<4 (sim), ou seja, o bloco e executado, o while imprime "0" e faz j=0+1=1
#Na segunda vez: testa se j<4 (sim), ou seja, imprime "1" e faz j=1+1=2
#Na terceira vez: testa se j<4 (sim), ou seja, imprime "2" e faz j=2+1=3
#Na quarta vez: testa se j<4 (sim), ou seja, imprime "3" e faz j=3+1=4
#Na quinta vez: testa se j<4 (nao), ou seja, nao executa o bloco.
#   Para auxiliar a utilizacao desses lacos, existem os comandos "break" e "continue". 
#   O break serve para parar a execucao de um laco e geralmente e utilizado dentro de um comando condicional.
for k in xrange(5):   #k assume os valores dentro da lista [0,1,2,3,4]
  print k             #imprime o valor contido em k
  if k == 3:          #se o valor de k for igual a 3 executa o bloco abaixo
    break             #encerra o loop
#Ou seja, k assume os valores 0,1,2 e 3 e imprime estes. Apos imprimir "3", o comando break e executado e o laco e encerrado sem 
#que k assuma o valor 4.
#   O continue serve para que a execucao do laco pule para o proximo valor da lista e geralmente e utilizado dentro de um comando
#condicional tambem.
for l in xrange(5):   #l assume os valores dentro da lista [0,1,2,3,4]
  if l == 3:          #se o valor de l for igual a 3 executa o bloco abaixo
    continue          #pula a execucao do resto do bloco do for e l assume o proximo valor na lista
  print l             #imprime o valor contido em l
#   Ou seja, l assume os valores 0,1,2,3 e 4. Porem imprime apenas 0,1,2 e 4, pois quando l assume o valor 3 o comando de impressao
#e pulado pelo comando continue.
#   Por ultimo, podemos utilizar, tambem, o comando "else" para um laco. Quando o else e utilizado, o bloco que ele contem e 
#executado caso a condicao de execucao do laco de False. O bloco do else e executado mesmo que haja um comando continue no bloco
#do laco, porem nao e executado caso o laco seja encerrado por um break.
m=0               #declara o inteiro m que assume o valor 0
while m < 5:      #enquanto m for menor que 5 executa o bloco abaixo
  if m == 4:      #se m for igual a 4 executa o bloco abaixo
    m=m+1         #soma 1 no valor de m
    continue      #continua para a proxima execucao do laco
  print m         #imprime o valor contido em 
  m=m+1           #soma 1 no valor de m
else:             #caso a condicao do while assuma o valor False o bloco abaixo e executado
  print "A condicao do laco assumiu o valor logico 'False'!"    #imprime a string entre aspas
#Durante a execucao desse laco, sao impressos "0", "1", "2" e "3" e a string acima.
while m > 0:      #enquanto m for maior que 0 executa o bloco abaixo
  if m == 3:      #caso m assuma o valor 3 executa o bloco abaixo
    break         #encerra o laco
  print m         #imprime o valor contido em m
  m=m-1           #diminui 1 no valor de m
else:             #caso a condicao do while assuma o valor False o bloco abaixo e executado
  print "Xablaw"  #imprime a string "Xablaw"
#durante a execucao desse laco, sao impressos "5" e "4". Quando m assume o valor 3 o laco e encerrado e o bloco do else tambem
#nao e executado.

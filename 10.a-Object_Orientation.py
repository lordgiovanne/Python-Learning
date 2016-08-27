#   O estudo da orientação a objetos e de extrema importancia pro aprendizado em python. Bascamente, python e uma linguagem de programacao
#baseada em orientacao a objetos. De certa forma, todos os tipos de variaveis que utiliamos ate agora sao objetos.
#   Primeiro, precisamos entender dois conceitos basicos: classe e objeto. 
#   Uma classe e a definicao de uma estrutura que pode conter atributos (atributos sao objetos, porem podemos enxerga-los como variaveis
#em uma primeira intancia) e metodos (que sao como funcoes).
#   Um objeto é uma estrutura de uma determinada classe. Um exemplo que podemos utilizar para faciliar o entendimento é o seguinte:
#   Iremos criar a classe "heroi" e entao os objetos "thor", "batman" e "blackwidow" pertencentes a classe heroi. Vamos fazer com que os 
#herois tenham 2 atributos principais: superpoderes (uma lista de strings com os poderes dos herois, em caso de um heroi nao ter
#superpoderes a lista nao tera elementos) e vida (uma string indicando se o heroi esta em perigo ou esta seguro). Alem dessas 
#caracteristicas, cada heroi tera o metodo "salvar" que altera o estado de um outro heroi de pergigo para seguro caso o primeiro nao 
#esteja em perigo.
#   Primeiramente iremos definir a classe heroi utilizando a seguinte sintaxe:
class  heroi:                   #aqui damos o nome "heroi" a classe           
  superpoderes = []             #aqui dizemos que dentro dessa classe existe atributo "superpoderes" que e uma lista
  vida = "seguro"               #aqui dizemos que dentro dessa classe existe atributo "vida" que e uma string
  
  def salvar(self, heroi):      #aqui definimos o metodo "salvar" da classe heroi
    if self.vida == "seguro":   #aqui verificamos se a vida do objeto que utiliza o metodo e "seguro"
      if heroi.vida == "perigo":  #aqui verificamos se o heroi a ser salvo esta em perigo
        heroi.vida = "seguro"     #caso sim, o heroi passado como parametro tem a vida alterada para "seguro"
        print "Salvamento efetuado com sucesso"     #imprimimos uma mensagem de sucesso
    else :                      #caso o primeiro if nao seja verificado como true
      print "Nao foi possivel efetuar o salvamento" #imprimimos uma mensagem de falha
#   Agora que ja definimos a classe heroi, vamos criar nossos objetos e atribuir os atributos deles.
thor = heroi()                  #aqui criamos o objeto "thor"
batman = heroi()                #aqui criamos o objeto "batman"
blackwidow = heroi()            #aqui criamos o objeto "blackwidow"
thor.superpoderes.append("forca")   #aqui incluimos "forca" aos poderes de thor
thor.superpoderes.append("voo")     #aqui incluimos "voo" aos poderes de thor
thor.superpoderes.append("raio")    #aqui incluimos "raio" aos poderes de thor
batman.superpoderes.append("preparo")   #aqui incluimos "preparo aos poderes de batman"
thor.vida = "perigo"            #aqui alteramos o atributo vida de thor para "perigo"
#O assunto continua no proximo tutorial...

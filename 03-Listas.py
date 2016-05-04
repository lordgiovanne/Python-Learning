#   Listas sao basicamente um conjunto de variaveis ordenadas por indices. Estas variaveis precisam ser do mesmo tipo.
#E importante observar que o primeiro termo da lista recebe o indice 0 e nao 1. Por exemplo, temos a declaracao da lista
#"lista_inteiros" e da lista "lista_strings" a seguir:

lista_inteiros = [1,2,3,4]
lista_strings = ["oi","tudo","bem","tchau"]

#   Agora imprimimos a posicao de indice 3 de ambos os vetores e observamos que corresponde ao quarto termo da lista...

print(lista_inteiros[3]) #voce pode testar no learnpython e vera que o programa imprime "4"
print(lista_strings[3])  #o programa imprime "tchau"

#   Para adicionar um novo termo na lista, basta utilizar o comando "nome_da_lista.append(termo_a_ser_adicionado)". Por ex:

lista_inteiros.append(5)
lista_strings.append("adicionado")

#   Agora conferimos os termos adicionados:

print(lista_inteiros[4]) #imprime "5"
print(lista_strings[4])  #imprime "adicionado"

#   E importante notar que e possivel sintaticamente tentar acessar um termo que nao existe na lista, nesses casos o programa
#ao ser submetido ao interpretador ira gerar uma mensagem de erro. Portanto, tome cuidado para nao faze-lo. Por ex:

print(lista_inteiros[5]) #essa linha gera um erro, pois nao existe a sexta posicao na lista

#   Tente executar o programa e observe a mensagem de erro, em seguida altere o indice para algum existente na lista e observe
#que o programa volta a funcionar normalmente

#Proximo assunto: operadores.

#Copiando uma lista para a outra ( Atribuindo Valor)

lista = [1,2,3,4]
listab = lista
listab.append(5)
print(lista)
print(listab)

#A listab passa a referencia a lista a, assim sendo qualquer alteração transforma as duas

#Clonando uma lista(Fatiando):
lista = [1,2,3,4]
listab = lista[:]#Copia todos os elementos de uma lista pra nova variavel(Quando trabalhamos com colchetes, sempre trabalhamos com elementos)
listab.append(5)
print(lista)
print(listab)
#Recuperando elementos da lista.

##Pra pegar um valor da lista, utilizamos o indicie que queremos:
lista = [1,2,3,4]
elemento1 = lista[0]
elemento2 = lista[1]
elemento3 = lista[2]
print(elemento1)
print(elemento2)
print(elemento3)

#Para recuperarmos mais de um elemento, vamos pegar uma fatia da lista
#Fatia funciona da seguinte maneira: 
#Queremos da posição x até a y
# Ou seja [Inicial (X) : Final (y)]
#Caso não tenha um dos valores na lista pegaremos tudo daquele 'lado', exemplo:
#Para lista de um até quatro lista[1:4]
#Para listas[:4] -> pegamos elementos até 4
#Para listas[2:] -> pegamos elementos entre 2 e tudo

lista = ['a','b','c','d','e','f','g','h','i','k']
#Posições[0-1-2-3-4-5-6-7-8-9]
um_teste = lista[1:4]#Entre  as posições 1 e 4
dois_teste = lista[:4]#Até a 4 posição
tres_teste = lista[2:]#A partir da 2° posição
print(um_teste)
print(dois_teste)
print(tres_teste)
#Sempre que trabalharmos com intervalos(range):
#O primeiro valor é inclusivo e o ultimo valor é exclusivo
# [:] De tudo até tudo
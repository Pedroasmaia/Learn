# É uma lista como objeto de lista, exemplo:
lista = [[1,2],[3,4]]
print(lista)

print(lista[0])#O Print do primeiro objeto da lista que contem a lista de 1 e 2
print(lista[1])#O Print do segundo objeto da lista que contem a lista de 3 e 4

#Agora se eu quiser pegar somente o numero 1 e o numero 4 faria assim:
print(lista[0][0])#Falando de que da Lista eu quero a primeira posição(que é a matriz [1,2]) e dentro dessa matriz eu quero também a primeira posição
print(lista[1][1])#Falando de que da Lista eu quero a segunda posição(que é a matriz [3,4]) e dentro dessa matriz eu quero também a segunda posição

# Ficando assim:

um = lista[0][0]
dois = lista[0][1]
tres = lista[1][0]
quatro = lista[1][1]

print(f'O primeiro objeto da primeira matriz contida da lista é {um}')
print(f'O segundo objeto da primeira matriz contida da lista é {dois}')
print(f'O primeiro objeto da segunda matriz contida da lista é {tres}')
print(f'O segundo objeto da segunda matriz contida da lista é {quatro}')

#Funções Nativas para listas

    # - Append() => Serve para fazer adicões no final das listas

more = ['um']
more.append('dois')
more.append('tres')
more.append('quatro')
print(more)

    # - Index() => Retorna o indice de um determinado elemento

Tvalhalla = ['Pedro','Thiago','Lucas','Matheus','Iury']
#Indices-------0---------1------2--------3--------4----|
indice_lucas = Tvalhalla.index('Lucas')
indice_pedro = Tvalhalla.index('Pedro')
print(indice_lucas)
print(indice_pedro)

    # *Extra* in() => Verifica se o elemento esta na lista

print('Pedro' in Tvalhalla)
print('Duda' in Tvalhalla)

    # - Insert()=> Insere um elemento na lista em uma determinada posição

animais = ['Gato','Cão']
#Indices-------0---1----|
animais.insert(1,'Furão')#Escolhido o Indice 1
print(animais)
 
    # -  Remove() => Serve pra remover determinado elemento

animais.remove('Gato')
print(animais)

    # - Pop() => Remove um elemento em um determinado indice, interagindo com a lista, apenas removendo o elemento do indice

animais.append('Leão')
animais.append('Zebra')
print(animais)
animais.pop(2)#Escolhido o Indice 2
print(animais)
animais.pop(2)#Escolhido o Indice 2
print(animais)

    # - del() => Remove um elemento passado por parametro

animais.append('Leão')
animais.append('Zebra')
del(animais[2])
print(animais)

    # - sort() => Ordena a lista interagindo a lista

lista = [1,3,9,2]
print(lista)
lista_sort = lista.sort()
print(lista_sort)

    # sorted() => Ordena a lista passada por parametro

embaralhada = [90,85,88,10]
organizada = sorted(embaralhada)
print(embaralhada)
print(organizada)
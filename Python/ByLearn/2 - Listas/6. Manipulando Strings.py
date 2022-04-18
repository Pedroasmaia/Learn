#Caractere é uma letra só
from os import truncate
import string


char = 'c'
# String é um 'conjunto' de caractere
string_palavra = 'Felipe'
string_frase = 'Aqui tem uma frase'

# Vetor (Array) => Sequencia de elementos do mesmo tipo
# String é um vetor (array) de caracteres
Nome = 'Pedro'

#------01234
print(Nome[0])#Vai mostrar P
print(Nome[1])#Vai mostrar e
print(Nome[2])#Vai mostrar d
print(Nome[3])#Vai mostrar r
print(Nome[4])#Vai mostrar o

#Strings são imutaveis, mas se fatiarmos podemos alterar o valor de algum indíce:
nova__palavra = Nome[:3] + 'a' + Nome[3:]
print(nova__palavra)

palavra ='abcdef'
print(palavra[-1])
print(palavra[-2])
print(palavra[:])

#É possivel pesquisar em string:

real = '5' in palavra

print(real)
real_2 = '5' not in palavra

print(real_2)

#Alterar entre minuscula para maiúsculo

minuscula = 'Pe' + 'DR'.lower() + 'o'.lower()
print(minuscula)

maiuscula = 'pedro'.upper()

print(maiuscula)

#Para saber o tamanho da string

print(len(maiuscula))


#Checar se são apenas letras

print('abc'.isalpha())
print('a1c'.isalpha())
print('a@c'.isalpha())

# Remover espaços em branco no inicio ou no fim

no_space = " sobrando espaços      "
print(no_space.strip())

#Juntar os niveis atraves de um delimitador

alfabeto = 'abcdefghijklmnopqrstuvx'

print(" | ".join(alfabeto))
print(" , ".join(alfabeto))
print(" / ".join(alfabeto))

#Separar uma string atraves de um delimitador
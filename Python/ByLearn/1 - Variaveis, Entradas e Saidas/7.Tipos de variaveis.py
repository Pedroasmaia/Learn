#Tipo da variavel define o comportamento e o entendimento da variavel
#Exemplo, podemos entender algo sendo como um número ou como um texto
# 23 é um numero ou um texto?
# "23" é um texto string
# 23 é um número int
# 23.0 também é um número

#para saber o tipo de uma variavel:

from unicodedata import decimal


text = '23'
number = 23
decimo = 23.99
print(type(text))
print(type(number))
print(type(decimo))

#Convertendo tipos:
#Na programação chamamos isso de cast
#para passar é so usar o tipo:
transform = int(decimo)
print(decimo)
print(transform)
